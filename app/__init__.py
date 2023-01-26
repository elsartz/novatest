from os import getenv
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from app.db import init_db, get_db
from app.models import Note
import json
import jsonpickle
from json import JSONEncoder

load_dotenv()

def create_app(test_config=None):
  # set up app config
  app = Flask(__name__, static_url_path='/')
  CORS(app)
  app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DB_URL')
  db = SQLAlchemy(app)
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    SECRET_KEY='super_secret_key'
  )
 

  init_db(app)

  @app.route('/notes', methods=['GET'])
  def get_notes():
    dbase = get_db()
    notes = dbase.query(Note).all()
   
    sampleJson = jsonpickle.encode(notes)
    json_data = json.loads(sampleJson)

    return jsonify(json_data)

  @app.route('/notes', methods=['POST'])
  def add_note():
    dbase = get_db()
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    note = Note(title, content)
    dbase.session.add(note)
    dbase.session.commit()
    return jsonify({'message': 'note added successfully'})

  @app.route('/notes/<id>', methods=['PUT'])
  def update_note(id):
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    note = Note.query.get(id)
    note.title = title
    note.content = content
    db.session.commit()
    return jsonify({'message': 'note updated successfully'})

  @app.route('/notes/<id>', methods=['DELETE'])
  def delete_note(id):
    dbase = get_db()
    # note = Note.query.get(id)
    note = dbase.query(Note).filter(Note.id == id).one()
    print(note)
    dbase.delete(note)
    # dbase.session.delete(note)
    dbase.commit()
    # db.session.commit()
    return jsonify({'message': 'note deleted successfully'})

  return app
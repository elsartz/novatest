from os import getenv
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.db import init_db, get_db
# from app.models import Note

load_dotenv()

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DB_URL')
# db = SQLAlchemy(app)

def create_app(test_config=None):
  # set up app config
  app = Flask(__name__, static_url_path='/')
  app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DB_URL')
  db = SQLAlchemy(app)

#   CORS(app)
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    SECRET_KEY='super_secret_key'
  )
 

  init_db(app)

#   class Note(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80))
#     content = db.Column(db.String(250))

#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

  @app.route('/notes', methods=['GET'])
  def get_notes():
    notes = Note.query.all()
    return jsonify({'notes': [note.__dict__ for note in notes]})

  @app.route('/notes', methods=['POST'])
  def add_note():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    note = Note(title, content)
    db.session.add(note)
    db.session.commit()
    return jsonify({'message': 'note added successfully'})

  @app.route('/notes/<int:id>', methods=['PUT'])
  def update_note(id):
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    note = Note.query.get(id)
    note.title = title
    note.content = content
    db.session.commit()
    return jsonify({'message': 'note updated successfully'})

  @app.route('/notes/<int:id>', methods=['DELETE'])
  def delete_note(id):
    note = Note.query.get(id)
    db.session.delete(note)
    db.session.commit()
    return jsonify({'message': 'note deleted successfully'})

  return app

# if __name__ == '__main__':
#     app.run(debug=True)

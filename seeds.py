from app.models import Note
from app.db import Session, Base, engine

# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()
# insert notes
db.add_all([
    Note(title='This is 1st title', content='This is a note'),
    Note(title='This is 2nd title', content='This is another note'),
    Note(title='This is a 3rd title', content='This is a third note'),
])

db.commit()
db.close()
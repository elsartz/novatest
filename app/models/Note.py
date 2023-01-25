from app.db import Base
from sqlalchemy import Column, Integer, String

class Note(Base):
  __tablename__ = 'notes'
  id = Column(Integer, primary_key=True)
  title = Column(String(80))
  content = Column(String(250))

  def __init__(self, title, content):
    self.title = title
    self.content = content
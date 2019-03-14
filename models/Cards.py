from sqlalchemy import Column, Integer, String, DateTime, Text
from Base import Base


class Cards(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True)
    word = Column(String(120))
    bucket = Column(Integer)
    wrong_count = Column(Integer)
    available = Column(DateTime)
    definition = Column(Text)

    def __init__(self, word=None, definition=None):
        self.word = word
        self.definition = definition

    def __repr__(self):
        return '<User %r>' % (self.word)

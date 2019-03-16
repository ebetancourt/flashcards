from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta

from models.Base import Base


class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True)
    word = Column(String(120))
    bucket = Column(Integer)
    wrong_count = Column(Integer)
    available = Column(DateTime)
    definition = Column(Text)

    BUCKET_INTERVALS = [
        0,  # Bucket 0
        timedelta(seconds=5),  # Bucket 1
        timedelta(seconds=25),  # Bucket 2
        timedelta(minutes=2),  # Bucket 3
        timedelta(minutes=10),  # Bucket 4
        timedelta(hours=1),  # Bucket 5
        timedelta(hours=5),  # Bucket 6
        timedelta(days=1),  # Bucket 7
        timedelta(days=5),  # Bucket 8
        timedelta(days=25),  # Bucket 9
        # Bucket 10 -- timedelta only goes up to days, not months and years
        timedelta(days=121),
        # Bucket 11, in 200 years is not technically NEVER, but might as well be
        timedelta(days=(200*365)),
    ]

    def __init__(self, word=None, definition=None, bucket=0, wrong_count=0, available=None):
        self.word = word
        self.definition = definition
        self.bucket = bucket
        self.wrong_count = wrong_count
        self.available = available

    def __repr__(self):
        return '<Card %r>' % (self.word)

    def mark_wrong(self):
        self.bucket = max(1, self.bucket - 1)
        self.wrong_count = self.wrong_count + 1
        self.set_next_available()

    def mark_right(self):
        self.bucket = min(11, self.bucket + 1)
        self.set_next_available()

    def set_next_available(self):
        self.available = datetime.now() + self.BUCKET_INTERVALS[self.bucket]

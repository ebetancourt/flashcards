from sqlalchemy import Column, Integer, String, DateTime, Text, or_
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta

from models.Base import Base
from app import db


class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True)
    word = Column(String(120))
    bucket = Column(Integer, default=0)
    wrong_count = Column(Integer, default=0)
    available = Column(DateTime, default=datetime.now())
    definition = Column(Text)
    user = Column(Integer, default=0)

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

    def time_til_available(self):
        if self.available is None:
            return 'Now'
        delta = self.available - datetime.now()
        if delta.total_seconds() < 0:
            return 'Now'

        if self.bucket == 11 or self.wrong_count >= 10:
            return 'Never'
        if delta.total_seconds() > (3600 * 24):
            return '{:d} days'.format(round(delta.total_seconds() / (3600 * 24)))
        if delta.total_seconds() > 3600:
            return '{:d} hours'.format(round(delta.total_seconds() / 3600))
        if delta.total_seconds() > 600:
            return '{:d} minutes'.format(round(delta.total_seconds() / 60))
        if delta.total_seconds() > 60:
            return '{:.1f} minutes'.format(delta.total_seconds() / 60)
        return '{:d} seconds'.format(round(delta.seconds))

    def save(self):
        if self.id is None:
            db.session.add(self)
        return db.session.commit()

    @staticmethod
    def get_next(user_id):
        return db.session.query(Card) \
            .filter(or_(Card.available < datetime.now(), Card.bucket == 0)) \
            .filter(Card.bucket < 11) \
            .filter(Card.user == user_id) \
            .order_by((Card.bucket != 0), Card.available) \
            .limit(1).first() \

    @staticmethod
    def find_by_id(id):
        return db.session.query(Card).get(id)

    @staticmethod
    def all_for_current_user(user_id):
        return db.session.query(Card) \
            .filter(Card.user == user_id) \
            .all()

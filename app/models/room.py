from sqlalchemy import Column, Integer, ForeignKey
from . import Base
from app.models.quizz import Quizz
from app.models.user import User

class Room(Base):
    __tablename__ = 'Room'
    id = Column(Integer, primary_key=True)
    creator = Column(Integer, ForeignKey('User.id'))
    quizz = Column(Integer, ForeignKey('Quizz.id'))
    has_begun = Column(Integer, default=0)

    # Inherited object method which displays chosen Object information (here the Client)
    def __repr__(self):
        return '<Quizz {}>'.format(self.title)

    def get_id(self):
        return self.id

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'creator': self.creator
        }

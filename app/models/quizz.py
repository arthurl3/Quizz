from sqlalchemy import Column, Integer, ForeignKey, String
from . import Base
from app.models.user import User

class Quizz(Base):
    __tablename__ = 'Quizz'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    creator = Column(Integer, ForeignKey('User.id'))

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

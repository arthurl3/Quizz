from app.models.user import User
from sqlalchemy import Column, Integer, ForeignKey
from . import Base

class Relationship(Base):
    __tablename__ = 'Relationship'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    friend_id = Column(Integer, ForeignKey('User.id'))

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'friend_id': self.friend_id
        }
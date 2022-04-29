from sqlalchemy import Column, Integer, ForeignKey
from . import Base
from app.models.user import User
from app.models.room import Room


class Player(Base):
    __tablename__ = 'Player'
    id = Column(Integer, primary_key=True)
    user_ref = Column(Integer, ForeignKey('User.id'))
    room_ref = Column(Integer, ForeignKey('Room.id'))

    # Inherited object method which displays chosen Object information (here the Client)
    def __repr__(self):
        return '<Player {}>'.format(self.user_ref)

    def get_id(self):
        return self.id

    def serialize(self):
        return {
            'id': self.id,
            'user_ref': self.user_ref,
            'room_ref': self.room_ref
        }

from sqlalchemy import Column, Integer, String
from app import Base

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    token = Column(String(255))

    # Inherited object method which displays chosen Object information (here the User)
    def __repr__(self):
        return '<User {}>'.format(self.name)


    def get_id(self):
        return self.id

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'token': self.token
        }

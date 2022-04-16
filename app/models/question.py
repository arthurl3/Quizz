from sqlalchemy import Column, Integer, ForeignKey, String
from app import Base

class Question(Base):
    __tablename__ = 'Question'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    phrase = Column(String(1000))

    # Inherited object method which displays chosen Object information (here the Client)
    def __repr__(self):
        return '<Question {}>'.format(self.title)

    def get_id(self):
        return self.id

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'phrase': self.phrase
        }

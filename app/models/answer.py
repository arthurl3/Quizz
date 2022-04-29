from sqlalchemy import Column, Integer, ForeignKey, String
from . import Base

class Answer(Base):
    __tablename__ = 'Answer'
    id = Column(Integer, primary_key=True)
    phrase = Column(String(80))
    is_true = Column(Integer, default=0)

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

from sqlalchemy.orm import declarative_base
from database import engine

Base = declarative_base()

from app.models.user import User
from app.models.answer import Answer
from app.models.player import Player
from app.models.question import Question
from app.models.quizz import Quizz
from app.models.relationship import Relationship
from app.models.room import Room
from logger import LOGGER

Base.metadata.create_all(engine)


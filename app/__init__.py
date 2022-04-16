import types
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Config
import socketio

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio)
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
from .models.relationship import Relationship as r1
from .models.quizz import Quizz as r2
from .models.question import Question as r3
from .models.user import User as r4
from .models.player import Player as r5
from .models.room import Room as r6
Base.metadata.create_all(engine)


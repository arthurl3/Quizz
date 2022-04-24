import app
from app.models.relationship import Relationship
from app.models.quizz import Quizz
from app.models.question import Question
from app.models.user import User
from app.models.player import Player
from app.models.room import Room

session = app.SessionLocal

### Execute la requête
def execute(data):
    session.add(data)
    session.commit()
    return data

#### INSERT INTO ###
#Association d'ami (toujours unilatéral)
def add_relationship(user, friend):
    data = Relationship(user_id=user.id, friend_id=friend.id)
    return execute(data)

#Crée un salon de jeu (Peut-etre faire rejoindre directement le créateur)
def add_room(user, quizz):
    data = Room(creator=user.id, quizz=quizz.id)
    return execute(data)

#Quand un user rejoint une room
def add_player(user, room):
    data = Player(user_ref=user.id, room_ref=room.id)
    return execute(data)

def add_quizz(quizz):
    return execute(quizz)

def add_question(question):
    return execute(question)

def add_user(user):
    return execute(user)

#### SELECT FROM ####
def get_user_by_username(username):
    return User.query.filter_by(username=username).one_or_none()

def get_user_by_token(token):
    return User.query.filter_by(token=token).one_or_none()

def get_room_by_user(user):
    return Room.query.filter_by(creator=user.id).one_or_none()

def get_quizz_by_user(user):
    return Room.query.filter_by(creator=user.id).all()


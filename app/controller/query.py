from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from logger import LOGGER
from app.models import Relationship
from app.models import Quizz
from app.models import Question
from app.models import User
from app.models import Player
from app.models import Room
from sqlalchemy.orm import Session


########## CREATE (INSERT INTO) #########
def create_user(session: Session, user: User) -> User:
    """
    Create a new user if username isn't already taken.
    :param session: SQLAlchemy database session.
    :type session: Session
    :param user: New user record to create.
    :type user: User
    :return: Optional[User]
    """
    try:
        existing_user = (
            session.query(User).filter(User.name == user.name).first()
        )
        if existing_user is None:
            session.add(user)  # Add the user
            session.commit()  # Commit the change
            LOGGER.success(f"Created user: {user}")
        else:
            LOGGER.warning(f"Users already exists in database: {existing_user}")
        return session.query(User).filter(User.name == user.name).first()
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when creating user: {e}")
        raise e

#Quand un user rejoint une room
def create_relationship(session: Session, relationship: Relationship) -> Relationship:
    """
    Create unilateral friendship between 2 users
    :param session: SQLAlchemy database session.
    :type session: Session
    :param user1: .
    :type user: User
    :return: Optional[User]
    """
    try:
        existing_relationship = (
            session.query(Relationship).filter(Relationship.user_id == relationship.user_id, Relationship.friend_id == relationship.friend_id).first()
        )
        if existing_relationship is None:
            session.add(relationship)  # Add the user
            session.commit()  # Commit the change
            LOGGER.success(f"Created relationship: {relationship}")
        else:
            LOGGER.warning(f"Users already exists in database: {existing_relationship}")
        return session.query(Relationship).filter(Relationship.user_id == relationship.user_id, Relationship.friend_id == relationship.friend_id).first()
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when creating user: {e}")
        raise e

##Crée un salon de jeu (Peut-etre faire rejoindre directement le créateur)
def create_room(session: Session, room: Room) -> Room:
    """
    Create unilateral friendship between 2 users
    :param session: SQLAlchemy database session.
    :type session: Session
    :param user1: .
    :type user: User
    :return: Optional[User]
    """
    try:
        existing_room = (
            session.query(Room).filter(Room.creator == room.creator).first()
        )
        if existing_room is None:
            session.add(room)  # Add the user
            session.commit()  # Commit the change
            LOGGER.success(f"Created relationship: {room}")
        else:
            LOGGER.warning(f"Users already exists in database: {existing_room}")
        return session.query(Room).filter(Room.creator == room.creator).first()
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when creating user: {e}")
        raise e



def create_player(session: Session, player: Player) -> Player:
    """
    Create unilateral friendship between 2 users
    :param session: SQLAlchemy database session.
    :type session: Session
    :param user1: .
    :type user: User
    :return: Optional[User]
    """
    try:
        existing_player = (
            session.query(Player).filter(Player.user_ref == player.user_ref).first()
        )
        if existing_player is None:
            session.add(player)  # Add the user
            session.commit()  # Commit the change
            LOGGER.success(f"Created relationship: {player}")
        else:
            LOGGER.warning(f"Users already exists in database: {existing_player}")
        return session.query(Room).filter(Room.creator == player.creator).first()
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when creating user: {e}")
        raise e

# Pas d'édition de quizz pour l'instant
# def create_quizz(session: Session, quizz: Quizz) -> Quizz:
#     """
#     Create unilateral friendship between 2 users
#     :param session: SQLAlchemy database session.
#     :type session: Session
#     :param user1: .
#     :type user: User
#     :return: Optional[User]
#     """
#     try:
#         existing_quizz = (
#             session.query(Quizz).filter(Quizz.creator == quizz.creator).first()
#         )
#         if existing_player is None:
#             session.add(player)  # Add the user
#             session.commit()  # Commit the change
#             LOGGER.success(f"Created relationship: {player}")
#         else:
#             LOGGER.warning(f"Users already exists in database: {existing_player}")
#         return session.query(Room).filter(Room.creator == player.creator).first()
#     except IntegrityError as e:
#         LOGGER.error(e.orig)
#         raise e.orig
#     except SQLAlchemyError as e:
#         LOGGER.error(f"Unexpected error when creating user: {e}")
#         raise e
#
# def add_question(question):
#     return execute(question)

# Pas d'édition de quizz pour l'instant
# def create_question(session: Session, question: Question) -> Question:
#     """
#     Create unilateral friendship between 2 users
#     :param session: SQLAlchemy database session.
#     :type session: Session
#     :param user1: .
#     :type user: User
#     :return: Optional[User]
#     """
#     try:
#         existing_quizz = (
#             session.query(Quizz).filter(Quizz.creator == quizz.creator).first()
#         )
#         if existing_player is None:
#             session.add(player)  # Add the user
#             session.commit()  # Commit the change
#             LOGGER.success(f"Created relationship: {player}")
#         else:
#             LOGGER.warning(f"Users already exists in database: {existing_player}")
#         return session.query(Room).filter(Room.creator == player.creator).first()
#     except IntegrityError as e:
#         LOGGER.error(e.orig)
#         raise e.orig
#     except SQLAlchemyError as e:
#         LOGGER.error(f"Unexpected error when creating user: {e}")
#         raise e
#
# def add_question(question):
#     return execute(question)
###############################



#### MORE COMPLEX REQUESTS ####
###############################

#### BASIC GETTERS ####
def get_user_by_username(session: Session, uname) -> User:
    user = None
    """
    Create unilateral friendship between 2 users
    :param session: SQLAlchemy database session.
    :type session: Session
    :param user1: .
    :type user: User
    :return: Optional[User]
    """
    try:
        user = session.query(User).filter(name=uname).one_or_none()
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when getting user: {e}")
        raise e
    else:
        return user

def get_user_by_token(session: Session, token) -> User:
    user = None
    """
    Create unilateral friendship between 2 users
    :param session: SQLAlchemy database session.
    :type session: Session
    :param user1: .
    :type user: User
    :return: Optional[User]  
    """
    try:
        user = session.query(User).filter(token=token).one_or_none()
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when getting user: {e}")
        raise e
    else:
        return user

def get_room_by_user(session: Session, user: User) -> Room:
    room = None
    """
    Create unilateral friendship between 2 users
    :param session: SQLAlchemy database session.
    :type session: Session
    :param user1: .
    :type user: User
    :return: Optional[User]  
    """
    try:
        room = session.query(Room).filter(creator=user.id).one_or_none()
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when getting user: {e}")
        raise e
    else:
        return room

def get_quizz_by_user(session: Session, user: User) -> Quizz:
    quizz = None
    """
    Create unilateral friendship between 2 users
    :param session: SQLAlchemy database session.
    :type session: Session
    :param user1: .
    :type user: User
    :return: Optional[User]  
    """
    try:
        quizz = session.query(Quizz).filter(creator=user.id).one_or_none()
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when getting user: {e}")
        raise e
    else:
        return quizz


# A def :
def get_players_by_room():
    pass
def get_users_by_players():
    pass
def get_questions_by_quizz():
    pass
def get_friends():
    pass

### UPDATE ###

#


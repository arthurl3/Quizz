"""Purge all data from database."""
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from database import session
from logger import LOGGER


def cleanup_data():
    try:
        session.execute(text("PRAGMA FOREIGN_KEY = OFF;"))
        session.commit()
        session.execute(text("DELETE FROM answer;"))
        session.commit()
        session.execute(text("DELETE FROM player;"))
        session.commit()
        session.execute(text("DELETE FROM question;"))
        session.commit()
        session.execute(text("DELETE FROM quizz;"))
        session.commit()
        session.execute(text("DELETE FROM relationship;"))
        session.commit()
        session.execute(text("DELETE FROM room;"))
        session.commit()
        session.execute(text("DELETE FROM user;"))
        session.commit()
        session.execute(text("PRAGMA FOREIGN_KEY = OFF;"))
        session.commit()
        LOGGER.success("Successfully reset all data.")
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when resetting data: {e}")
        raise e
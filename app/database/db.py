from app import sessionmaker, Base
import sqlite3
from config import Config


def init_db():
    connection = sqlite3.connect(Config.SQLALCHEMY_DATABASE_URI)

    with open('fill_db.sql') as f:
        connection.executescript(f.read())

    c = connection.cursor()
    connection.commit()
    connection.close()
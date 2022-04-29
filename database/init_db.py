from database import session, objects
from app.models import *

def fill_database():
    users = objects.create_users()
    session.add_all(users)
    session.commit()

    relationships = objects.create_relationships()
    session.add_all(relationships)
    session.commit()

    questions = objects.create_questions()
    session.add_all(questions)
    session.commit()

    quizz = objects.create_quizz()
    session.add_all(quizz)
    session.commit()


from app.models import *

'''
Fichier test de remplissage de la DB
'''


def create_users():
    users = []

    u1 = User(
        name='Ronan#8451',
        token='yjBVantB1k5j7fxEDi3tJ3hhm845jaXGjor'
    )
    u2 = User(
        name='Hitler#6485',
        token='  vWdALW7RB4hjk6bUB3jxio4RIptOqzlKlma'
    )
    u3 = User(
        name='Poutine#6894',
        token='urpNu3yKA3IKFsVIaYkYlJN9jlMCFR7Y8nz'
    )

    users.append(u1)
    users.append(u2)
    users.append(u3)
    return users

def create_relationships():
    relationships = []

    r1 = Relationship(
     user_id=2,
     friend_id=1
    )
    r2 = Relationship(
     user_id=3,
     friend_id=1
    )

    relationships.append(r1)
    relationships.append(r2)
    return relationships

def create_questions():
    questions = []

    q1 = Question(
        title = "Un beau bilan",
        phrase = "Combien de morts à Auschwitz",
        quizz = 1
    )
    q2 = Question(
        title = "Un peu d'amour",
        phrase = "Quelle est la taille moyenne d'un pénis français",
        quizz=1
    )
    q3 = Question(
        title = "Une grosse tour",
        phrase = "Quelle est la taille de la tour Eiffel",
        quizz=1
    )

    questions.append(q1)
    questions.append(q2)
    questions.append(q3)

    return questions

def create_quizz():
    quizz = []

    q1 = Quizz(title='Golden shower', creator=1)
    quizz.append(q1)
    return quizz







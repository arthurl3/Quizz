import random
import string
import secrets


#Genere un token de longueur k
def generate_token(k):
    return ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=k))

# A faire  : checker dans la BDD si c'est pas déjà pris
def generate_username(user):
    n = random.randint(1000, 9999)
    return f'{user}#{n}'

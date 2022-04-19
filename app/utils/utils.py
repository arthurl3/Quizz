import random
import string
import secrets


#Genere un token de longueur k
def generate_token(k):
    return ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=k))
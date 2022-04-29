import json
from app.models import *

class Message:
    HELLO = 'hello'
    FIRST_CONNECTION = 'first'

    def first_connection(self, user):
        return json.dumps(
            {
                'username': user.name,
                'token': user.token
             }
        )

    def hello(self, user):
        return json.dumps(
            {
                'connected': 1
            }
        )

    def disconnect(self, user):
        return json.dumps(
            {
                'connected': 0
            }
        )







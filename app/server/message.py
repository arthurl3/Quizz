import json
from app.models import *

class Message:
    HELLO = 'hello'
    FIRST_CONNECTION = 'first'
    GET_ALL_QUIZZ = 'get_all_quizz'

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

    def get_all_quizz(self, all_quizz):
        '''
        return quizz list to a json array :
        [{
        'id': 1,
        'title':'quizzTitle',
        'img':???,
        },
        {
        'id':2,
        ...
        },
        ...
        ]
        '''
        return json.dumps(

        )







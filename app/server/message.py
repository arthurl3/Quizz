import json
from app.models import *

class Message:
    CONNECT = 'connect'
    FIRST_CONNECTION = 'first_connection'
    DISCONNECT = 'Disconnect'
    GET_ALL_QUIZZ = 'get_all_quizz'
    CREATE_ROOM = 'create_room'
    JOIN_ROOM = 'join_room'
    ADD_FRIEND = 'add_friend'


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

    def create_room(self, room):
        pass

    def join_room(self, room):
        pass







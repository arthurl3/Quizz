import socketio
import json
from app.controller.controller import Controller
from app.utils.utils import generate_token, generate_username
from app.server.message import Message

class QuizzServer(socketio.AsyncNamespace):
    sio = socketio.AsyncServer(async_mode='asgi')
    app = socketio.ASGIApp(sio)
    controller = Controller()
    msg = Message()

    def __init__(self):
        self.call_backs()

    def call_backs(self):
        @self.sio.event
        async def connect(sid, environ, auth=None):
            # Condition 1 :  si token et username reçu, c'est un utilisateur connu
            if 'token' in auth in auth:
                token = auth['token']
                user = self.controller.connect(sid, token)
                response = self.msg.hello(user)
                await self.sio.emit(self.msg.HELLO, response, to=sid)
            # Condition 2 : si seulement username est reçu, c'est la première fois qu'un utilisateur se connecte
            elif 'username' in auth:
                username = auth['username']
                username = generate_username(username)
                token = generate_token(35)
                user = self.controller.first_connection(sid, username, token)
                response = self.msg.first_connection(user)
                print(username)
                print(response)
                await self.sio.emit(self.msg.FIRST_CONNECTION, response, to=sid)
            else:
                raise ConnectionRefusedError('authentication failed')

        @self.sio.event
        async def disconnect(sid):
            self.controller.disconnect(sid)
            print('disconnected', sid)

        # Handle room creation
        # Data : {quizz: id}
        @self.sio.event
        async def get_all_quizz(sid, data):
            all_quizz = self.controller.get_all_quizz(sid)
            response = self.msg.get_all_quizz(all_quizz)
            print('room created', sid)

        # Handle room creation
        # Data : {quizz: id}
        @self.sio.event
        async def create_room(sid, data):
            quizz_id = data['quizz']
            room = self.controller.create_room(sid, quizz_id)
            print('room created', sid)

        # Handle a user who join a friend room
        # Data : { friend: id }
        @self.sio.event
        async def join_room(sid, data):
            friend_id = data['friend']
            join_room(sid, friend_id)
            print('room joined', sid)

        # Handle an add friend request
        # Data : { friend: id }
        @self.sio.event
        async def add_friend(sid, data):
            print('friend added', sid)

        @self.sio.event
        def message(sid, data):
            print(data)

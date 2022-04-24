import socketio
import json
from app.controller.controller import Controller
from app.utils.utils import generate_token
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
            if 'token' in auth and 'username' in auth:
                token = auth['token']
                username = auth['username']
                response = self.msg.hello()
                await self.sio.emit(self.msg.HELLO, response, to=sid)
            # Condition 2 : si seulement username est reçu, c'est la première fois qu'un utilisateur se connecte
            elif 'username' in auth:
                token = generate_token(35)
                username = auth['username']
                print(username)
                response = self.msg.first_connection(token)
                print(response)
                await self.sio.emit(self.msg.FIRST_CONNECTION, response, to=sid)
            else:
                raise ConnectionRefusedError('authentication failed')


        @self.sio.event
        async def disconnect(sid):
            print('disconnected', sid)

        @self.sio.event
        def message(sid, data):
            print(data)

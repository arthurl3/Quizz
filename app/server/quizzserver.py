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
            #print(f'connected sid={sid}')
            print(environ)
            if 'token' in auth and 'username' in auth:
                token = auth['token']
                username = auth['username']
                to_send = self.msg.hello()
                await self.sio.emit(self.msg.HELLO, to_send, to=sid)
            elif 'username' in auth:
                token = generate_token(35)
                username = auth['username']
                print(username)
                to_send = self.msg.first_connection(token)
                print(to_send)
                await self.sio.emit(self.msg.FIRST_CONNECTION, to_send, to=sid)
            else:
                raise ConnectionRefusedError('authentication failed')

        @self.sio.event
        async def disconnect(sid):
            print('disconnected', sid)

        @self.sio.event
        def message(sid, data):
            print(data)

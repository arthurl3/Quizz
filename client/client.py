import asyncio
import socketio

sio = socketio.AsyncClient()


@sio.event
async def connect():
    print("Connected")


@sio.event
async def disconnect():
    print('disconnected from server')


@sio.event
def hello(data):
    print(data)

@sio.event
def fist_connection(data):
    print(data)

async def start_server():
    await sio.connect('http://localhost:5000', auth={'username' : 'ronan'})
    #await sio.emit('message', {'foo': 'bar'})
    await sio.wait()


if __name__ == '__main__':
    asyncio.run(start_server())
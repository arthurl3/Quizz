from app import sio

@sio.event
async def connect(sid, environ, auth):
    print(f'connected auth={auth} sid={sid}')
    await sio.emit('hello', (1, 2, {'hello': 'you'}), to=sid)

@sio.event
def disconnect(sid):
    print('disconnected', sid)
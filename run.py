import uvicorn
from app.server.quizzserver import QuizzServer

if __name__ == '__main__':
    qs = QuizzServer()
    uvicorn.run(qs.app, host='127.0.0.1', port=5000)




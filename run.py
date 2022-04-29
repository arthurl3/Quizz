import uvicorn
#from app.server.quizzserver import QuizzServer
from database import init_script

if __name__ == '__main__':
    init_script()
    #qs = QuizzServer()
    #uvicorn.run(qs.app, host='127.0.0.1', port=5000)




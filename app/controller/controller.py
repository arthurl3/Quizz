import database
from app.models.user import User
from app.controller import query

class Controller():
    user_map = {}

    def __init__(self):
        pass

    # Handle first connection by setting token and username in the database
    def first_connection(self, sid, username, token):
        user = User(name=username, token=token)
        user = query.create_user(user)
        if user:
            self.user_map[sid] = user
            return user

    # Connection via token
    def connect(self, sid, token):
        user = query.get_user_by_token(token)
        if user:
            self.user_map[sid] = user
            return user

    # Disconnect a user bien deleted his entry in user_map dict
    def disconnect(self, sid):
        del self.user_map[sid]

    def create_room(self, sid):
        pass

    def set_user(self, sid, token):
        self.user_map[sid] = query.get_user_by_token(token)

    def set_token(self, sid, token):
        user = self.user_map[sid]
        user.token = token

    def join_room(self, sid, friend):
        user = self.user_map[sid]
        room = friend.room












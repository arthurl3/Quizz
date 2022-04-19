import json


class Message:
    HELLO = 'hello'
    FIRST_CONNECTION = 'first'

    def first_connection(self, token):
        return json.dumps(
            {'token': token}
        )

    def hello(self, username):
        return json.dumps(
            {'username': username}
        )



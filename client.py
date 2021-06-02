from typing import Optional

from connection import Connection


class ChatClient:
    def __init__(self, nickname: str):
        self.nickname = nickname
        self._connection: Optional[Connection] = None
        self._last_msg_index = 0

    def send_message(self, message: str):
        sent_message = f'{self.nickname}:{message}'
        self.connection.broadcast(sent_message)
        return sent_message

    def fetch_messages(self):
        messages = list(self.connection.get_messages())
        new_message = messages[self._last_msg_index:]
        self._last_msg_index = len(messages)
        return new_message

    @staticmethod
    def _get_connection():
        return Connection(('localhost', 9090))

    @property
    def connection(self):
        if self._connection is None:
            self._connection = ChatClient._get_connection()
        return self._connection

    @connection.setter
    def connection(self, new_connection: Connection):
        if self._connection is not None:
            self._connection.close()
        self._connection = new_connection

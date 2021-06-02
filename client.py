from typing import Optional

from connection import Connection


class ChatClient:
    def __init__(self, nickname: str, connection_provider=Connection):
        self.nickname = nickname
        self._connection: Optional[Connection] = None
        self._connection_provider = connection_provider
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

    @property
    def connection(self):
        if self._connection is None:
            self._connection = self._connection_provider(('localhost', 9090))
        return self._connection


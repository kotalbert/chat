from multiprocessing.managers import SyncManager
from typing import Any


class Connection(SyncManager):

    def __init__(self, address: Any):
        self.register('get_messages')
        super().__init__(address=address, authkey=b'my_chat_secret')
        self.connect()

    def broadcast(self, message: str):
        messages = self.get_messages()
        messages.append(message)

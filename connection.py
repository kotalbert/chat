from multiprocessing.managers import SyncManager, ListProxy
from typing import Any


class Connection(SyncManager):

    def __init__(self, address: Any):
        self.register('get_messages', proxytype=ListProxy)
        super().__init__(address=address, authkey=b'my_chat_secret')
        self.connect()

    def broadcast(self, message: str):
        messages = self.get_messages()
        messages.append(message)

    def get_messages(self):
        return []

    def close(self):
        pass


class FakeServer:
    def __init__(self):
        self._last_command = None
        self._last_args = None
        self._messages = []


    def __call__(self, *args, **kwargs):
        """
        Make SyncManager think that a new connection was created
        """

        return self

    def send(self, data):
        """
        Track commands that was sent to the server.
        """
        call_id, command, args, kwargs = data
        self._last_command = command
        self._last_args = args

    def recv(self, *args, **kwargs):
        """
        Send back the server response to the client.
        """

        lc = self._last_command
        if lc == 'dummy':
            return '#RETURN', None
        if lc == 'create':
            return '#RETURN', ('fake_id', tuple())
        if lc == 'append':
            self._messages.append(self._last_args[0])
            return '#RETURN', None
        if lc == '__contains__':
            return '#RETURN', self._last_args[0] in self._messages
        if lc in ('incref', 'decref', 'accept_connection'):
            return '#RETURN', None

        return '#ERROR', ValueError(f'{self._last_command} - {self._last_args}')

    def close(self):
        pass

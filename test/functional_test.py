import unittest
from multiprocessing.managers import SyncManager, ListProxy

from client import ChatClient

# implement chat server for acceptance test
_messages = []


def _srv_get_messages():
    return _messages


class _ChatServerManager(SyncManager):
    pass


_ChatServerManager.register('get_messages', callable=_srv_get_messages, proxytype=ListProxy)


def new_chat_server():
    return _ChatServerManager(('', 9090), authkey=b'my_chat_secret')


class TestChatFunctional(unittest.TestCase):
    def test_message_exchange(self):
        """
        Chat clients should be able to exchange messages between each other.
        """

        with new_chat_server():
            albert = ChatClient("Albert")
            arwena = ChatClient("Arwena")

            albert.send_message("Hello, give food.")
            messages = arwena.fetch_messages()

            self.assertListEqual(["Hello, give food"], messages)

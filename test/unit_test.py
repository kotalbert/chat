import unittest
from unittest.mock import Mock, patch

from client import ChatClient
from connection import Connection


class TestChatClient(unittest.TestCase):

    def test_nickname(self):
        """
        Chat Client should return user nickname.
        """
        client = ChatClient('Albert')
        self.assertEqual(client.nickname, 'Albert')

    def test_send_message(self):
        """
        Client should sent message in appropriate format.
        """
        client = ChatClient('Albert')
        client.connection = Mock()
        sent_message = client.send_message('Give food')
        self.assertEqual(sent_message, 'Albert:Give food')


class TestConnection(unittest.TestCase):

    def test_broadcast(self):
        with patch.object(Connection, 'connect'):
            c = Connection(('localhost', 9090))

        with patch.object(c, 'get_messages', return_value=[]):
            c.broadcast('some message')
            self.assertIn('some message', c.get_messages())

    @patch.object(ChatClient, '_get_connection')
    def test_client_connection(self, get_connection_mock):
        client = ChatClient('Albert')
        client.send_message('Give food.')
        connection_spy = get_connection_mock()
        connection_spy.broadcast.assert_called_with('Albert:Give food.')

    def test_exchange_with_server(self):
        """
        Connections should use the same server to communicate.
        """

        c1 = Connection(('localhost', 9090))
        c2 = Connection(('localhost', 9090))

        c2.broadcast('connected message')
        self.assertIn('some message', c1.get_messages())
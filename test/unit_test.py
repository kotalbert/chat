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

    @patch.object(Connection, '_get_connection')
    def test_client_connection(self, connection_spy):
        client = ChatClient('Albert')
        client.send_message('Give food.')

        self.assertTrue(connection_spy.broadcast.assert_called_with('Albert:Give food.'))

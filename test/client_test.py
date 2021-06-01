import unittest

from client import ChatClient


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
        sent_message = client.send_message('Give food')
        self.assertEqual(sent_message, 'Albert:Give food')

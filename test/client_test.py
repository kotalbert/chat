import unittest


class TestChatClient(unittest.TestCase):

    def test_nickname(self):
        """
        Chat Client should return user nickname.
        """
        client = ChatClient('Albert')
        self.assertEqual(chat.nickname, 'Albert')

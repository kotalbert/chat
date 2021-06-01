import unittest

from client import ChatClient


class TestChatFunctional(unittest.TestCase):
    def test_message_exchange(self):
        """
        Chat clients should be able to exchange messages between each other.
        """
        albert = ChatClient("Albert")
        arwena = ChatClient("Arwena")

        albert.send_message("Hello, give food.")
        messages = arwena.fetch_messages()

        self.assertListEqual(["Hello, give food"], messages)


if __name__ == '__main__':
    unittest.main()

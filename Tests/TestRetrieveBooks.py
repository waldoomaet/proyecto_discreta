import unittest
import random
import os
from Class.APIService import APIService

class TestRetrieveBooks(unittest.TestCase):

    def test_that_sending_valid_bookshelf_name_returns_list_of_books(self):
        input_str = "a"
        bookshelf = APIService.retrieve_books(input_str)
        if bookshelf:
            index = random.randint(0, len(bookshelf) - 1)
            self.assertTrue(bookshelf[index].name is not None)
        else:
            self.fail(f"Bookshelf didn't return a list of Book: {bookshelf}")

    def test_sending_empty_bookshelf_name_returns_None(self):
        input_str = ""
        bookshelf = APIService.retrieve_books(input_str)
        self.assertIsNone(bookshelf)

    def test_sending_request_without_network_returns_None(self):
        input_str = 'a'
        try:
            # Disables system's wifi connection
            os.system("netsh interface set interface 'Wifi' disabled")
            bookshelf = APIService.retrieve_books(input_str)
            self.assertIsNone(bookshelf)

        except AssertionError as err:
            # Enables system's wifi again and then throws exception
            os.system("netsh interface set interface 'Wifi' enabled")
            raise err

if __name__ == '__main__':
    unittest.main()
import unittest
from Class.Bookshelf import Bookshelf

class TestBinarySearch(unittest.TestCase):

    def test_that_searching_for_a_valid_name_in_bookshelf_returns_book(self):
        input_str = "LIFE"
        bookshelf = Bookshelf('a')
        bookshelf.sort_books()
        self.assertTrue(bookshelf.find_book(input_str).name == input_str)

    def test_that_searching_for_a_invalid_name_returns_None(self):
        input_str = "Not in the bookshelf"
        bookshelf = Bookshelf('a')
        bookshelf.sort_books()
        self.assertIsNone(bookshelf.find_book(input_str))
    
    def test_that_searching_for_an_empty_name_returns_None(self):
        input_str = ""
        bookshelf = Bookshelf('a')
        bookshelf.sort_books()
        self.assertIsNone(bookshelf.find_book(input_str))

if __name__ == '__main__':
    unittest.main()
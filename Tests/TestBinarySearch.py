import unittest
from Class.Bookshelf import Bookshelf

class TestBinarySearch(unittest.TestCase):

    def test_that_searching_for_a_valid_name_in_bookshelf_returns_book(self):
        input_str = "LIFE"
        try:
            bookshelf = Bookshelf('a')
            bookshelf.sort_books()
            self.assertTrue(bookshelf.find_book(input_str).name == input_str)
        
        except Exception as err:
            self.fail(f"Exception raised unexpectedly {str(err)}")

    def test_that_searching_for_a_invalid_name_returns_None(self):
        input_str = "Not in the bookshelf"
        try:
            bookshelf = Bookshelf('a')
            bookshelf.sort_books()
            self.assertIsNone(bookshelf.find_book(input_str))
        
        except Exception as err:
            self.fail(f"Exception raised unexpectedly {str(err)}")
    
    def test_that_searching_for_an_empty_name_returns_None(self):
        input_str = ""
        try:
            bookshelf = Bookshelf('a')
            bookshelf.sort_books()
            self.assertIsNone(bookshelf.find_book(input_str))
        
        except Exception as err:
            self.fail(f"Exception raised unexpectedly {str(err)}")

if __name__ == '__main__':
    unittest.main()
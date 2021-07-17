import unittest
from Class.Bookshelf import Bookshelf

class TestMergeSort(unittest.TestCase):

    def test_that_given_valid_list_of_books_list_of_books_is_sorted(self):
        input_str = 'a'
        bookshelf = Bookshelf(input_str)
        bookshelf.sort_books()
        for index in range(len(bookshelf.books) - 1):
            self.assertLess(bookshelf.books[index].name, bookshelf.books[index + 1].name)

    def test_that_sort_can_handle_empty_list_of_books(self):
        input_str = 'a'
        bookshelf = Bookshelf(input_str)
        bookshelf.books = []
        bookshelf.sort_books()
        self.assertFalse(bool(bookshelf.books))

if __name__ == '__main__':
    unittest.main()
from typing import List
from Class.Book import Book
from Class.APIService import APIService
from typing import List


class Bookshelf:
    def __init__(self, name:str = None) -> None:
        self.name = ""
        self.books = []
        if name:
            self.name = name
            self.books = APIService.retrieve_books(name)

    @staticmethod
    def __merge_sort(list: List[Book]) -> List[Book]:
        if len(list) > 1:
            mid = len(list) // 2
            L = list[:mid]
            R = list[mid:]
            L = Bookshelf.__merge_sort(L)
            R = Bookshelf.__merge_sort(R)
            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i].name < R[j].name:
                    list[k] = L[i]
                    i += 1
                else:
                    list[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                list[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                list[k] = R[j]
                j += 1
                k += 1

        return list

    def __binary_search(list: List[Book], l: int, r: int, x: str) -> Book:
        while l <= r:
            mid = l + (r - l) // 2
            if list[mid].name == x or x in list[mid].name:
                return list[mid]
            elif list[mid].name < x:
                l = mid + 1
            else:
                r = mid - 1
        return None

    def sort_books(self) -> None:
        self.books = Bookshelf.__merge_sort(self.books)


    def find_book(self, name:str) -> Book:
        return Bookshelf.__binary_search(self.books, 0, len(self.books) - 1, name)
from Class.Book import Book
from Class.Author import Author
import requests
import json
from typing import List


class APIService:
    count = 1

    @staticmethod
    def __get_books_from_api(to_search: str, page_count: str) -> object:
        url = f"https://www.googleapis.com/books/v1/volumes?q={to_search}&maxResults=40" \
          f"&startIndex={page_count}&key=AIzaSyBPodNvYCBfimpOhj4cnOodPjG1sCj3L34"
        return json.loads((requests.get(url)).content)


    @classmethod
    def retrieve_books(cls, word: str) -> List[Book]:
        # Saves the response
        response = APIService.__get_books_from_api(word, 0)

        if "items" in response.keys():
            raw_books = response["items"]
            books = []
            for book in raw_books:
                title = book["volumeInfo"]["title"].upper()
                description = book["volumeInfo"]["description"] if "description" in book["volumeInfo"] else None
                published_date = book["volumeInfo"]["publishedDate"] if "publishedDate" in book["volumeInfo"] else None
                author = Author(book["volumeInfo"]["authors"]) if "authors" in book["volumeInfo"] else None
                books.append(Book(cls.count, title, description, published_date, author))
                cls.count += 1
            return books
        
        else:
            raise Exception("Something went wrong calling api")
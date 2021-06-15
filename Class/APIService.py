from Class.Book import Book
from Class.Author import Author
import requests
import json

class APIService:
    @staticmethod
    def __get_books_from_api(to_search: str, page_count: str) -> object:
        url = f"https://www.googleapis.com/books/v1/volumes?q={to_search}&maxResults=40" \
          f"&startIndex={page_count}&key=AIzaSyBPodNvYCBfimpOhj4cnOodPjG1sCj3L34"
        return json.loads((requests.get(url)).content)


    @staticmethod
    def retrive_books(word: str) -> list[Book]:
        # Saves the response
        response = APIService.__get_books_from_api(word, 0)

        if "items" in list(response.keys()):
            raw_books = response["items"]
            books = []
            for book in raw_books:
                volumen_info_keys = list(book["volumeInfo"].keys())
                title = book["volumeInfo"]["title"] if "title" in volumen_info_keys else ""
                description = book["volumeInfo"]["description"] if "description" in volumen_info_keys else ""
                published_date = book["volumeInfo"]["publishedDate"] if "publishedDate" in volumen_info_keys else ""
                author = Author(", ".join(book["volumeInfo"]["authors"])) if "authors" in volumen_info_keys else None
                books.append(Book(title, description, published_date, author))
            return books
        
        else:
            raise Exception("Something went wrong calling api")
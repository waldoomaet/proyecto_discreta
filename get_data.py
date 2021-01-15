import requests
import json
from string import ascii_lowercase
import pickle
from pathlib import Path


# Just keep in mind that this function returns the response of the API query
def get_books_from_api(toSearch, pageCount):
    url = f"https://www.googleapis.com/books/v1/volumes?q={toSearch}&maxResults=40&startIndex={pageCount}&key" \
          f"=your_key "
    return json.loads((requests.get(url)).content)


# This checks if exists any pickle file
def is_there_pickle():
    path = Path("data.pkle")
    return path.exists()


def retrieve_books(fromUrl=False):
    books = {}
    # If true, go find books using API
    if fromUrl:
        # This iterates over every letter in the alphabet
        for word in ascii_lowercase:
            # Prettier
            print('.', end='')

            # Saves the response
            response = get_books_from_api(word, 0)

            # Luckly the API returns the total of records that matched the search
            bookCount = response['totalItems']
            addedBooks = 0

            # Just keep in mind that this get all the books
            while addedBooks < bookCount:
                if "items" in list(response.keys()):
                    booksNow = len(response['items'])
                    addedBooks += booksNow
                    for book in response['items']:
                        if "title" in list(book["volumeInfo"].keys()):
                            books[book["volumeInfo"]["title"]] = ''
                    response = get_books_from_api(word, addedBooks)
                else:
                    break

        # To avoid repeated records being efficient, the books were saved as a dict
        # so now we get all the keys from that dict
        books = list(books.keys())

        try:
            # After that save the records in a pickle file for later use
            file = open("data.pkle", "wb")
            pickle.dump(books, file)
            file.close()

        except:
            print(books)

    # Else, just open pickle file (MUCH faster and doesn't have a daily limit)
    else:
        file = open("data.pkle", "rb")
        books = pickle.load(file)
        file.close()

    return books

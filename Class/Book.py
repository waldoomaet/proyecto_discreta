from Class.Author import Author

class Book:
    # Indice para los libros, para facilitar sorting
    def __init__(self, name:str, description:str, published_date:str, author:Author):
        self.name = name
        self.description = description
        self.published_date = published_date
        self.author = author
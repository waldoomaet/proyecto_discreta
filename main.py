from Class.Book import Book
from Class.Bookshelf import Bookshelf
from string import ascii_lowercase
import time

allowedInputs = ["printcmds", "printall", "printcount", "printrange", "searchbyname", "searchbyid", "end"]

# Lista de comandos

# "printcmds"                   -> Imprime todos los comandos
# "printall"                    -> Imprime todos los libros
# "printrange <start> <end>"    -> Imprime todos los libros entre start y end
# "printcount"                  -> Imprime el total de libros
# "searchbyname <name>"         -> Busca el nombre de un libro y devuelve el indice en lista
# "searchbyid <id>"             -> Toma un indice y devuelve el respectivo nombre
# "end"                         -> Gets out of the console

# Prettier
print("Buscando data...", end='')

# This gets the books
bookshelfs: list[Bookshelf] = []
for letter in "a":
    bookshelf = Bookshelf(letter)
    bookshelf.sort_books()
    bookshelfs.append(bookshelf)

# Prettier
print("\nOrganizando data...")

while True:
    inp = input("\ncmd>").lower()
    
    if "end" in inp:
        break
    
    elif "printcmds" in inp:
        for cmd in allowedInputs:
            print(f"> {cmd}")

    elif "printall" in inp:
        for bookshelf in bookshelfs:
            for book in bookshelf.books:
                print(f"* {book.name}")

    elif "printcount" in inp:
        count = 0
        for bookshelf in bookshelfs:
            count += len(bookshelf.books)
        print(count)

    elif "printrange" in inp:
        try:
            # Gets lower bound of the first number
            lowerBound = inp.find(' ') + 1

            # Gets upper bound of the first number
            upperBound = inp.find(' ', len("printrange") + 2)

            # Gets first number
            begin = int(inp[lowerBound:upperBound])

            # Gets second number
            end = int(inp[upperBound + 1:])

            id_range = range(begin, end)
            books = []

            if begin < end:
                for bookshelf in bookshelfs:
                    for book in bookshelf.books:
                        if book.id in id_range:
                            books.append(book)
                for book in books:
                    print(f"* {book.name}")
            else:
                print("Inicio debe de ser mayor y distinto al final")

        except Exception:
            # In case the command parameters are weird
            print("El comando falló...")

    
    elif "searchbyid" in inp:
        try:
            # Gets lower bound of the first number
            to_find = int(inp[inp.find(' ') + 1:])
            id_found = -1

            for bookshelf in bookshelfs:
                for book in bookshelf.books:
                    if book.id == to_find:
                        print(book.name)
                        break

            print("Ningun nombre asociado a este id")

        except Exception:
            # In case the command parameters are weird
            print("El comando falló...")
    
    elif "searchbyname" in inp:
        # Gets lower bound of the first number
        to_find = inp[inp.find(' ') + 1:].upper()

        for bookshelf in bookshelfs:
            # Binary search
            book = bookshelf.find_book(to_find)
            if book is not None:
                print(f"Libro en la posicion {book.id}")
                break
        
        print("Palabra no encontrada")
    
    else:
        print("Comando invalido")

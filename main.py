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
print("Buscando data", end='')

# This gets the books
bookshelfs: list[Bookshelf] = []
for letter in "abc":
    bookshelfs.append(Bookshelf(letter))

# Prettier
print("\nOrganizando data...")

# Sorting data
for bookshelf in bookshelfs:
    bookshelf.sort_books()
    print(bookshelf.find_book("Injertando a Dioniso").__dict__)

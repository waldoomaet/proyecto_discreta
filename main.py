import get_data
import Sort
import Search
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

# This gets the books. If there is no pickle file then go find the books with the API
data = get_data.retrieve_books() if get_data.is_there_pickle() else get_data.retrieve_books(True)

# Prettier
print("\nOrganizando data...")
start = time.time()

# Sorting data
data = Sort.merge_sort(data)
print(f"Ordenado en {round(time.time() - start, 3)} segundos")

while True:
    inp = input("\ncmd>")

    if inp == "printcmds":
        for i in range(1, len(allowedInputs)):
            print(f"* {allowedInputs[i]}")

    elif inp == "printall":
        for element in data:
            print(f"* {element}")

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

            if begin < end:
                for element in data[begin:end]:
                    print(f"* {element}")
            else:
                print("Inicio debe de ser mayor y distinto al final")

        except Exception:
            # In case the command parameters are weird
            print("El comando falló...")

    elif inp == "printcount":
        print(len(data))

    elif "searchbyid" in inp:
        try:
            # Gets lower bound of the first number
            toFind = int(inp[inp.find(' ') + 1:])

            if toFind < len(data):
                start = time.time()
                print(data[toFind])
                print(f"Busqueda realizada en {round(time.time() - start, 3)} segundos")
            else:
                print("Ningun nombre asociado a este id")

        except Exception:
            # In case the command parameters are weird
            print("El comando falló...")

    elif "searchbyname" in inp:
        # Gets lower bound of the first number
        toFind = inp[inp.find(' ') + 1:]

        start = time.time()

        # Binary search
        word = Search.binary_search(data, 0, len(data) - 1, toFind)

        if word != -1:
            print(f"Libro en la posicion {word}")
            print(f"Busqueda realizada en {time.time() - start} segundos")
        else:
            print("Palabra no encontrada")

    elif inp == "end":
        break

    else:
        print("Comando invalido")

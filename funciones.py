import json
libros = []
#funciones
def agregar_libro():
    print("\tAgregar libro")
    title = input("Ingrese título: ")
    author = input ("Ingrese autor: ")
    year = int(input("Ingrese año de publicación: "))
    genre = input("Ingrese género: ")
    book ={
        "title":title,
        "author":author,
        "year":year,
        "genre":genre,
    }
    libros.append(book)
    print("Libro creado!")

def mostrar_libros():
    if not libros:
        print("No existen libros, tragedia!")
    else:
        print("\tLista de libros")
        for li in libros:
            print("Título: ", li["title"])
            print("Autor: ", li["author"])
            print("Año: ", li["year"])
            print("Género: ", li["genre"])
            print("(>'-'<)")

def buscar_libro():
    if not libros:
        print("No existen libros, tragedia!")
    else:
        print("\tBusqueda de libros")
        title_search = input("Inserte título a buscar: ")
        for li in libros:
            if title_search.lower() == li["title"].lower():
                print("Título: ", li["title"].capitalize())
                print("Autor: ", li["author"].title())
                print("Año: ", li["year"])
                print("Género: ", li["genre"])
                return
            
        print("Libro no existe!")


def modificar_libro():
    if not libros:
        print("No existen libros, tragedia!")
    else:
        print("\tModificación de libros")
        title_search = input("Inserte título a modificar: ")
        for li in libros:
            if title_search.lower() == li["title"].lower():
                li["author"] = input("Ingrese nuevo autor: ")
                li["year"] = int(input("Ingrese nuevo año: "))
                li["genre"] = input("Ingrese nuevo género: ")
                print("Libro modificado :3")
                return
        print("Libro no existe!")

def exportar_libro():
    if not libros:
        print("No existen libros, tragedia!")
    else:
        try:
            name_file = input("Ingrese nombre del archivo: ") + ".json"
            with open(name_file, "x") as file:
                json.dump(libros, file)
            print("Archivo creado! :3")
        except:
            print("Error! Ese archivo ya existe T__T")
def salir():
    print("Gracias! ^__^")

def eliminar_libro():
    if not libros:
        print("No existen libros, tragedia!")
    else:
        print("\tEliminar libro")
        title_search = input("Inserte título a buscar: ")
        for li in libros:
            if title_search.lower() == li["title"].lower():
                
                return
            
        print("Libro no existe!")
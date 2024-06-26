libros = []
import json
#funciones
def agregar_libro():
    print('\tAgregar libro')
    titulo = str(input('Ingrese el titulo del libro: '))
    autor = str(input('Ingrese el autor: '))
    anio = int(input('Ingrese el año del libro: '))
    genero = str(input('Ingrese el genero: '))
    libro = {
        "titulo":titulo,
        "autor":autor,
        "anio":anio,
        "genero":genero
    }

    libros.append(libro)
    print('LIBRO CREADO!')

def mostrar_libros():
    import time
    if not libros:
        print('NO EXISTEN LIBROS, FAVOR AGREGUE ALGUNO!')
    else:
        print("\t Lista Libros")
        for l in libros:
            print(f"\tTitulo: {l["titulo"]}\tAutor: {l["autor"]}\tAño: {l["anio"]}\tGenero: {l["genero"]}\n")
            time.sleep(4)
def buscar_libro():
    if not libros:
        print('NO EXISTEN LIBROS, FAVOR AGREGUE ALGUNO!')
    else:
        print("\t Lista Libros")
        titulo_buscar = str(input('Ingrese el titulo del libro a buscar: '))

        for l in libros:
            if titulo_buscar.lower() == l["titulo"].lower():
                print(f"\tTitulo: {l["titulo"].capitalize()}\tAutor: {l["autor"].title()}\tAño: {l["anio"]}\tGenero: {l["genero"]}\n")
                break
            else:
                print('El libro no se encuentra registrado!')
def modificar_libro():
      if not libros:
        print('NO EXISTEN LIBROS, FAVOR AGREGUE ALGUNO!')
      else:
        print("\t Lista Libros")
        titulo_mod = str(input('Ingrese el titulo del libro a modificar: '))

        for l in libros:
            if titulo_mod.lower() == l["titulo"].lower():
                l["autor"] = str(input('Ingrese un nuevo autor: '))
                l["anio"] = int(input('Ingrese nuevo año de publicacion: '))
                l["genero"] = str(input('Ingrese nuevo genero: '))
                print('Libro modificado!')
                return 
        print('LIBRO NO ENCONTRADO!')

def exportar_libro():
    if not libros:
        print('No existen libros, favor ingrese uno!')
    else:
        nombre_archivo = str(input('Ingrese el nombre del archivo: '))+".json"
        try:
            with open(nombre_archivo,"x") as archivo:
                json.dump(libros, archivo, indent=1)
            print("ARCHIVO CREADO!")
        except:
            print('ERROR! el nombre del archivo ya existe!')

# funcion extra
def eliminar_libro():
    if not libros:
        print('NO EXISTEN LIBROS, FAVOR AGREGUE ALGUNO!')
    else:
        print("\t Lista Libros")
        titulo_eliminar = str(input('Ingrese el titulo del libro a eliminar: '))

        for l in libros:
            if titulo_eliminar.lower() == l["titulo"].lower():
                libros.remove(l)
                print('Libro eliminado')
                return
            print('Libro no existe!')

    

def salir():
    import time
    import os
    for x in range(1,4):
        print('Saliendo de app biblioteca',("."*x))
        time.sleep(1)
        os.system('cls')

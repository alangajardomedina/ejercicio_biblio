libros = []
#funciones
def agregar_libro():
    print('\tAgregar libro: ')
    titulo=input('INgrese el título: ')
    autor=input('Ingrese autor: ')
    anio=int(input('Ingrese el año de lanzamiento: '))
    genero=input('Ingrese el género: ')
    libro={'titulo':titulo,
           'autor':autor,
           'anio':anio,
           'genero':genero}
    libros.append(libro)
    print('LIBRO AÑADIDIO...')



def mostrar_libros():
    print('Mostrar libros: ')
    if not libros:
        print('No hay libros..')
    else:
        print('\tLista de libros')
        for li in libros:        #li seria cada libro, en este caso, li seria un diccionario
            print('Libro: ',li['titulo'])
            print('Autor: ',li['autor'])
            print('Año de publicación: ',li['anio'])
            print('Género: ',li['genero'])
            print()



def buscar_libro():
    if not libros:
        print('No hay libros..')
    else:
        print('\tBuscar libros')
        titulo_buscar=input('Ingrese titulo a buscar: ')
        for li in libros:        #li seria cada libro, en este caso, li seria un diccionario
            if titulo_buscar.lower() == li['titulo'].lower():
                print('Titulo: ',li['titulo'].capitalize())
                print('Autor: ',li['autor'].title())
                print('Año de publicación: ',li['anio'])
                print('Género: ',li['genero'])
                print()
                return
        print()    
def modificar_libro():
        if not libros:
            print('No hay libros..')
        else:
            print('\tModificar libros')
            titulo_modificar=input('Ingrese titulo a modificar: ')
            for li in libros:        #li seria cada libro, en este caso, li seria un diccionario
                if titulo_modificar.lower() == li['titulo'].lower():
                    li['autor'] = input('Ingrese nuevo autor: ')
                    li['anio'] = int(input('Ingrese nuevo año: '))
                    li['genero'] = input('Ingrese nuevo genero: ')
                    print('LIBRO MODIFICADO ...')
                    break


def exportar_libro():
    if not libros:
        print('No hay libros.')
    else:
        nombre_archivo=input('Ingrese nombre de el archivo: ')+'.json'
        try:
            import json
            with open(nombre_archivo,'x') as archivo: 
                json.dump(libros, archivo, indent=1)
            print('ARCHIVO CREADO...')    
        except:
            print('Error, el nombre de el archivo ya existe..')    



def salir():
    print('ADIOOS...')
    exit()
#Funcion extra
def eliminar_libro():
    if not libros:
        print('No hay libros..')
    else:
        print('\tEliminar libros')
        titulo_eliminar=input('Ingrese titulo a eliminar: ')
        for li in libros:        #li seria cada libro, en este caso, li seria un diccionario
            if titulo_eliminar.lower() == li['titulo'].lower():
                libros.remove(li)
                print('LIBRO ELIMINADO...')
                return
        print() 

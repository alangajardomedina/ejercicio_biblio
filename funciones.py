libros = []
#funciones
def agregar_libro():
    print('\tAGREGAR LIBRO')
    titulo = input('Ingrese titulo: ')
    autor = input('Ingrese autor: ')
    anio = int(input('Ingrese año: '))
    genero = input('Ingrese genero: ')
    libro = {"titulo":titulo, "autor":autor, "anio":anio, "genero":genero}
    libros.append(libro)
    print('LIBRO CREADO')
def mostrar_libros():
    if not libros:
        print('No existen libros, agrege en la opcion 1')
    else:
        print('\tLISTA LIBROS')   
        for li in libros:
            print('TITULO:', li["titulo"])
            print('AUTOR:', li["autor"])
            print('AÑO:', li["anio"])
            print('GENERO:', li["genero"])
def buscar_libro():
    if not libros:
        print('No existen libros, agrege en la opcion 1')
    else:
        print('\tBUSCAR LIBROS') 
        titulo_nombre = input('Ingrese el titulo a buscar: ')  
        for li in libros:
            if titulo_nombre.lower() == li["titulo"].lower():
                print('TITULO:', li["titulo"].capitalize())
                print('AUTOR:', li["autor"])
                print('AÑO:', li["anio"])
                print('GENERO:', li["genero"])
                return
        print('LIBRO NO EXISTE')
def modificar_libro():
    if not libros:
        print('No existen libros, agrege en la opcion 1')
    else:
        print('\tMODIFICAR LIBROS') 
        titulo_modificado = input('Ingrese el titulo a modificar: ')  
        for li in libros:
            if titulo_modificado.lower() == li['titulo'].lower():
                li['autor'] = input('Ingrese nuevo autor: ')
                li['anio'] = input('Ingrese nuevo año: ')
                li['genero'] = input('Ingrese nuevo genero: ')
                print('libro modificado')
                return
        print('LIBRO NO EXISTE')
            
def exportar_libro():
    if not libros:
        print('NO EXISTEN LIBRO, ingrese en la opcion 1')
    else:
        import json
        try:
            nombre_tituilo = input('Ingres nombre del archivo: ')+'.json'
            with open (nombre_tituilo,"x") as archivo:
                json.dump(libros, archivo, indent=1)
            print("ARCHIVO CREADO!")
        except:
            print('ERROR, EL ARCHIVO YA EXISTE')

def salir():
    print('GRACIAS, ADIOS')
    exit()

def eliminar_libro():
    if not libros:
        print('No existen libros, agrege en la opcion 1')
    else:
        print('\tELIMINAR LIBRO') 
        titulo_eliminar = input('Ingrese el titulo a buscar: ')  
        for li in libros:
            if titulo_eliminar.lower() == li["titulo"].lower():
                libros.remove(li)
                print('Libro eliminado')
                return
    print('LIBRO NO EXISTE')
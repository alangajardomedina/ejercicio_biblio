libros = []
#funciones
def agregar_libro():
    print("AGREGAR LIBRO")
    titulo = input("Ingrese título: ")
    autor = input("Ingrese autor: ")
    anio = int(input("Ingrese año de publicación: "))
    genero = input("Ingrese género: ")
    libro = {"titulo":titulo, "autor":autor, "anio":anio, "genero":genero}
    libros.append(libro)
    print("LIBRO CREADO!")
def mostrar_libros():
    if not libros:
        print("NO EXISTEN LIBROS, porfavor agregue un libro")
    else:
        print("\tLISTA DE LIBROS")
        for li in libros:
            print("TÍTULO:", li["titulo"])
            print("AUTOR:", li["autor"])
            print("AÑO:", li["anio"])
            print("GÉNERO:", li["genero"])
            print()

def buscar_libro():
    if not libros:
        print("NO EXISTEN LIBROS, porfavor agregue un libro")
    else:
        print("\tBUSCAR DE LIBROS")
        titulo_buscar = input("Ingrese el título a buscar:")
        for li in libros:
            if titulo_buscar.lower==li["titulo"].lower():
                print("TÍTULO:", li["titulo"])
                print("AUTOR:", li["autor"])
                print("AÑO:", li["anio"])
                print("GÉNERO:", li["genero"])
                return
            print("LIBRO NO EXISTE!")

def modificar_libro():
    if not libros:
        print("NO EXISTEN LIBROS, porfavor agregue un libro")
    else:
        print("\tMODIFICAR DE LIBROS")
        titulo_modificar = input("Ingrese el título a modificar:")
        for li in libros:
            if titulo_modificar.lower==li["titulo"].lower():
                li["autor"] = input("Ingrese nuevo autor: ")
                li["anio"] = int(input("Ingrese nuevo año: "))
                li["genero"] = input("Ingrese nuevo género: ")
                print("\tLIBRO MODIFICADO!")
                break

def exportar_libro():
    if not libros:
        print("NO EXISTEN LIBROS, porfavor agregue un libro")
    else:
        nombre_archivo = input("Ingrese nombre del archivo: ")+".json"
        try:
            import json
            with open(nombre_archivo,"x") as archivo:
                json.dump(libros, archivo, indent=4)
            print("ARCHIVO CREADO!")
        except:
            print("ERROR, EL NOMBRE DEL ARCHIVO YA EXISTE!")
def salir():
    print("GRACIAS, ADIOS!")
    exit()

def eliminar_libro():
    if not libros:
        print("NO EXISTEN LIBROS, porfavor agregue un libro")
    else:
        print("\tELIMINAR LIBROS")
        titulo_eliminar = input("Ingrese el título a eliminar:")
        for li in libros:
            if titulo_eliminar.lower==li["titulo"].lower():
                libros.remove(li)
                print("LIBRO ELIMINADO!")
                return
            print("LIBRO NO EXISTE!")
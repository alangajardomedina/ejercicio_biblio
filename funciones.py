libros = []
#funciones
def agregar_libro():
    print("AGREGAR LIBRO")
    titulo = input("Ingrese titulo: ")
    autor = input("Ingrese autor: ")
    anio = int(input("Ingrese año de publicacion: "))
    genero = input("Ingrese genero: ")
    libro = {"titulo":titulo, "autor":autor, "anio":anio, "genero":genero}
    libros.append(libro)
    print("LIBRO CREADO!")
def mostrar_libros():
    if not libros:
        print("NO EXISTEN LIBROS, PORFAVOR AGREGUE ALGUNO!")
    else:
        print("\tLISTA DE LIBROS")
        for li in libros:
            print("TITULO:", li["titulo"])
            print("AUTOR:", li["autor"])
            print("AÑO:", li["anio"])
            print("GENERO:", li["genero"])
            print()
def buscar_libro():
    if not libros:
        print("NO EXISTEN LIBROS, PORFAVOR AGREGUE ALGUNO!")
    else:
        print("BUSCAR LIBRO")
        titulo_buscar = input("Ingrese titulo del libro a buscar: ")
        for li in libros:
            if titulo_buscar.lower==li["titulo"].lower():
                print("TITULO:", li["titulo"].capitalize())
                print("AUTOR:", li["autor"].title())
                print("AÑO:", li["anio"])
                print("GENERO:", li["genero"])
                return
        print("LIBRO NO EXISTE")
def modificar_libro():
    if not libros:
        print("NO EXISTEN LIBROS, PORFAVOR AGREGUE ALGUNO!")
    else:
        print("MODIFICAR LIBROS")
        titulo_modificar = input("Ingrese titulo del libro a modificar: ")
        for li in libros:
            if titulo_modificar.lower==li["titulo"].lower():
                li["autor"] = input("Ingrese nuevo autor: ")
                li["anio"] = input("Ingrese nuevo año de publicacion: ")
                li["genero"] = input("Ingrese nuevo genero: ")
                print("LIBRO MODIFICADO!")
                return
        print("LIBRO NO EXISTE")


def exportar_libro():
    if not libros:
        print("NO EXISTEN LIBROS, POR FAVOR AGREGUE ALGUNO!")
    else:
        nombre_archivo =input("Ingrese nombre dela archivo: ")+".json"
        try:
            import json
            with open(nombre_archivo,"x") as archivo:
                json.dump(libros, archivo, indent=1)
            print("ARCHIVO CREADO!")
        except:
            print("ERROR, EL NOMBRE DEL ARCHIVO YA EXISTE")
def salir():
    print("ADIOS")
    return
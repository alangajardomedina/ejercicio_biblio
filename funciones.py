libros = []

#funciones
def agregar_libro():
    print ("AGREGAR LIBRO")
    titulo = input("Ingrese Título: ")
    autor= input("Ingrese Autor")
    anio = int(input("Ingrese Año: "))
    genero = input("Ingrese Género: ")
    libro = {"Titulo":titulo, "autor":autor, "anio":anio, "genero":genero}
    libros.append(libro)
    print("LIBRO CREADO!")


def mostrar_libros():
    if not libros:
        print("NO EXISTEN LIBROS!, POR FAVOR AGREGUE ALGUNO")
    else:
        print("\t LISTA DE LIBROS")
        for li in libros:
            print("TÍTULO:", li["Titulo"])
            print("AUTOR:", li["autor"])
            print("AÑO:", li["anio"])
            print("GÉNERO:", li["genero"])
            print("-----------------")


def buscar_libro():
    if not libros:
        print("NO EXISTEN LIBROS!, POR FAVOR AGREGUE ALGUNO")
    else:
        print("\t BUSCAR LIBROS")
        titulo_buscar = input("Ingrese ítulo del libro que desee: ")

        for li in libros:
            if titulo_buscar.lower()==li["titulo"].lower():
                print("TÍTULO:", li["titulo"].capitalize())
                print("AUTOR:", li["autor"].title())
                print("AÑO:", li["anio"])
                print("GÉNERO:", li["genero"])
                return
        print("LIBRO NO EXISTE")
            
def modificar_libro():
    if not libros:
        print("NO EXISTEN LIBROS!, POR FAVOR AGREGUE ALGUNO")
    else:
        print("\t MODIFICAR LIBROS")
        titulo_modificar = input("Ingrese Título del libro a modificar: ")

        for li in libros:
            if titulo_modificar.lower()==li["titulo"].lower():
                li["autor"] = input("Ingerse nuevo autor: ")
                li["anio"] = int(input("Ingrese nuevo año: "))
                li["genero"] = input("Ingrese nuevo género: ")
                print("LIBRO MODIFICADO!")
                return
            

def exportar_libro():
    if not libros:
        print("NO EXISTEN LIBROS!, POR FAVOR AGREGUE ALGUNO")
    else:
        nombre_archivo = input("Ingrese NOmbre de su archivo: ")+".json"
        try:
            import json
            with open(nombre_archivo,"x") as archivo:
                json.dumb(libros, archivo, indent=3)
                print("ARCHIVO CREADO!")
            print("ARCHIVO CREADO")
        except:
            print("ERROR, EL NOMBRE DEL ARCHIVO YA EXISTE!")





def salir():
    
    print("GRACIAS POR PREFERIRNOS :)")
    
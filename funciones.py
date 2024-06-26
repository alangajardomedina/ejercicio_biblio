libros = []
#funciones
def agregar_libro():
    print("t\AGREGAR LIBRO")
    titulo = input("Ingrese título: ")
    autor = input("Ingrese autor: ")
    anio = int(input("Ingrese año de publcación : "))
    genero = input("Ingrese género: ")
    libro = {"titulo" :titulo, "autor": autor, "anio" : anio, "genero" : genero}
    libros.append(libro)
    print("LIBRO CREADO!")

def mostrar_libros():
    if not libros:
        print("NO EXISTEN LIBROS, FAVOR AGREGUE ALGUNO!")
    else:
        print("\tLISTA LIBROS")
        for li in libros: #li sería cada libro de la lista -> li: diccionario!
            print("TÍTULO: " , li["titulo"])
            print("AUTOR: " , li["autor"])
            print("AÑO: " , li["anio"])
            print("GÉNERO: ", li["genero"])
            print("")

def buscar_libro():
    if not libros:
        print("NO EXISTEN LIBROS, FAVOR AGREGUE ALGUNO!")
    else:
        print("\tBUSCAR LIBROS ") #primero
        titulo_buscar = input("ingrese título del libro a buscar: ")
        for li in libros: #li sería cada libro de la lista -> li: diccionario!
            if titulo_buscar.lower()==li ["título"].lower():
                print ("TÍTULO: " , li["titulo"].capitalize()):
                print("AUTOR: " , li["autor"])
                print("AÑO: " , li["anio"])
                print("GÉNERO: ", li["genero"])
                print("")

def modificar_libro():
    if not libros:
        print("NO EXISTEN LIBROS, FAVOR AGREGUE ALGUNO!")
    else:
        print("\tMODIFICAR LIBROS ") #primero
        titulo_modificar = input("ingrese título del libro a buscar: ")
        for li in libros: #li sería cada libro de la lista -> li: diccionario!
            if titulo_modificar.lower()==li ["título"].lower():
                li["autor"] = input("ingrese nuevo autor: ")
                li ["anio"] = int (input("ingrese nuevo año de publicación: "))
                li ["genero"] = (input("ingrese nuevo genero: "))
                print("LIBRO MODIFICADO!")

def exportar_libro():
    if not libros:
        print("NO EXISTEN LIBROS, FAVOR AGREGUE ALGUNO!")
    else:
        nombre_archivo = input("ingrese nombre del archivo: ")+".json"
        try:
            import json
            with open (nombre_archivo, "x") as archivo:
                json.dump(libros, archivo, indent=3)
            print("archivo creado!")
        except:
            print("error! el archivo ya existe!")

def salir():
    print("GRACIAS ADIOS!")

    exit()

def eliminar_libro():
    if not libros:
        print("NO EXISTEN LIBROS, FAVOR AGREGUE ALGUNO!")
    else:
        print("\tELIMINAR LIBROS ") 
        titulo_eliminar = input("ingrese título del libro a eliminar: ")
        for li in libros: 
            if titulo_eliminar.lower()==li ["título"].lower():
                libros.remove(li)
                print("LIBRO ELIMINADO!")
                return
            print("LIBRO NO EXISTE!")
            



                
    









libros = []
#import subprocess
#subprocess.run("shutdown -s")
#funciones
def agregar_libro():
    print ("\tAgrefar Libro")
    titulo = input("Ingrese Título: ")
    autor = input ("Ingrese autor: ")
    anio = int(input("Ingrese año de publicación: "))
    genero = input ("Ingrese género: ")
    libro = {"titulo":titulo,
             "autor":autor,
             "anio":anio,
             "genero":genero,
            }
    libros.append(libro)
    print("LIBRO AGREGADO")
def mostrar_libros():
    if not libros:
        print("No existen libros, agrege alguno!")
    else:
        print("\tLISTA LIBROS")
        for li in libros:
            print("TÍTULO:",li["titulo"])
            print("AUTOR:",li["autor"])
            print("AÑO:",li["anio"])
            print("GENERO:",li["genero"])
            print()
def buscar_libro():
    if not libros:
        print("No existen libros, agrege alguno!")
    else:
        print("\tBUSCAR LIBRO")
        titulo_buscar=input("Ingrese título a buscar: ")
        for li in libros:
            if titulo_buscar.lower==li["titulo"].lower():
                print("TÍTULO:",li["titulo"].capitalize())
                print("AUTOR:",li["autor"].title())
                print("AÑO:",li["anio"])
                print("GENERO:",li["genero"])
                return
        print("LIBRO NO EXCISTE")
def modificar_libro():
    if not libros:
        print("No existen libros, agrege alguno!")
    else:
        print("\tMODIFICAR LIBRO")
        titulo_modificar=input("Ingrese título a modificar: ")
        for li in libros:
            if titulo_modificar.lower==li["titulo"].lower():
                li["autor"] = input("Ingrese nuevo autor: ")
                li["anio"] = input("Ingrese nuevo año de publicacion: ")
                li["genero"] = input("Ingrese nuevo género: ")
                print("LIBRO MODIFICADO")
                return
        print("LIBRO NO EXCISTE")

def exportar_libro():
    if not libros:
        print("No existen libros, agrege alguno!")
    else:
        nombre_archivo = input("Ingrese nombre del archivo: ")+ ".json"
        try:
            import json
            with open (nombre_archivo,"w") as archivo:
                json.dump(libros, archivo, indent=2)
            print("ARCHIVO CREADO")
        except:
            print("ERROR! EL ARCHIVO YA EXCISTE")
    
def salir():
    print("Gracias, adios")
    exit()    
def eliminar_libro():
    if not libros:
        print("No existen libros, agrege alguno!")
    else:
        print("\tELIMINAR LIBRO")
        titulo_elimnar=input("Ingrese título a elminar: ")
        for li in libros:
            if titulo_elimnar.lower==li["titulo"].lower():
                libros.remove(li)
                print("LIBRO ELIMINADO")
                return
        print("LIBRO NO EXCISTE")
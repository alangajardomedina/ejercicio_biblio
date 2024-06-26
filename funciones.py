import os, time,json

libros = []
#funciones
def agregar_libro():
    print("AGREGAR LIBRO")
    titulo = input("Ingrese título del libro: ")
    autor = input("Ingrese autor del libro: ")
    anio = int(input("Ingrese año de publicación: "))
    genero = input("Ingrese género del libro: ")
    libro ={"Titulo":titulo,
            "Autor":autor,
            "Anio":anio,
            "Genero":genero}
    libros.append(libro)
    print("EL LIBRO A SIDO INGRESADO EXITOSAMENTE!")
    time.sleep(3) 
def mostrar_libros():
    if not libros:
        print("No hay libros ingresados...")
    else:
        print("LISTA DE LIBROS")
        for li in libros:
            print(f"Título: {li['Titulo']}, Autor: {li['Autor']}, Año: {li['Anio']}, Género: {li['Genero']}")
            print()

def buscar_libro():
    if not libros:
        print("No hay libros ingresados...")
    else:
        print("BUSCAR LIBRO")
        titulo_buscar = input("Ingrese título a buscar: ")
        for li in libros:
            if titulo_buscar.lower()==li["Titulo"].lower():
                print(f"Título: {li['Titulo']}, Autor: {li['Autor']}, Año: {li['Anio']}, Género: {li['Genero']}")
                time.sleep(3)
                return
        print("LIBRO NO ENCONTRADO!")

def eliminar_libro():
    if not libros:
        print("No hay libros ingresados...")
    else:
        print("ELIMINAR LIBRO")
        titulo_eliminar  = input("Ingrese título a eliminar: ")
        for li in libros:
            if titulo_eliminar.lower()==li["Titulo"].lower():
                libros.remove(li)
                print("LIBRO ELIMINADO")
                return
        print("LIBRO NO ENCONTRADO!")
        
            
        
def modificar_libro():
    if not libros:
        print("No hay libros ingresados...")
    else:
        print("MODIFICAR LIBRO")
        titulo_modificar  = input("Ingrese título a modificar: ")
        for li in libros:
            if titulo_modificar.lower()==li["Titulo"].lower():
                li["Autor"] = input("Ingrese nuevo autor: ")
                li["Anio"] = int(input("Ingrese nuevo año: "))
                li["Genero"] = input("Ingrese nuevo género: ")
                print("Libro modificado exitosamente!")
                time.sleep(3)
                return
        print("LIBRO NO ENCONTRADO!")
def exportar_libro():
    if not libros:
        print("No hay libros ingresados para exportar!")
    else:
        try:
            nombre_archivo = input("Ingrese nombre al archivo: ")+".json"
            with open (nombre_archivo,"x") as archivo:
                json.dump(libros, archivo, indent=2)
            print("ARCHIVO CREADO!")
        except:
            print("ERROR! El nombre del archivo ya existe!")
def salir():
    print("GRACIAS; A DIOS!")
    exit()
libros = []
#funciones
def agregar_libro():
    print("\t agregar libro")
    titulo = input("ingrese titulo: ")
    autor = input("ingrese autor")
    anio = int(input("ingrese año del libro: "))
    genero = input("ingrese el genero del libro: ")
    libro = {"titulo":titulo, "autor":autor, "anio":anio, "genero":genero}
    libros.append(libro)
    print("libro agregado")
def mostrar_libros():
    if not libros:
        print("no existen libros, favor de agregar libros!")
    else:
        print("\t lista libros")
        for li in libros:#li sería cada libro de la lista -> li: diccionario
            print("TITULO:", li["titulo"])
            print("AUTOR:", li["autor"])
            print("AÑO:", li["anio"])
            print("GENERO:", li["genero"])
            print()

def buscar_libro():
    if not libros:
        print("no existen libros, favor de agregar libros!")
    else:
        print("\t buscar libros") #se cambia el titulo al codigo de la opcion anterior 
        titulo_buscar = input("ingrece el titulo del libro: ")
        for li in libros:#li sería cada libro de la lista -> li: diccionario
            if titulo_buscar.lower()==li["titulo"].lower() : # se busca el libro en la lista
                print("TITULO:", li["titulo"].capitalize())
                print("AUTOR:", li["autor"].title())
                print("AÑO:", li["anio"])
                print("GENERO:", li["genero"])
                return
        print("libro no existe!")
    
def modificar_libro():
    if not libros:
        print("no existen libros, favor de agregar libros!")
    else:
        print("\t modificar libros") #se cambia el titulo al codigo de la opcion anterior 
        titulo_modificar = input("ingrece el titulo del libro")
        for li in libros:#li sería cada libro de la lista -> li: diccionario
            if titulo_modificar.lower()==li["titulo"].lower() : # se busca el libro en la lista
               li["autor"] = input("ingrese nuevo autor")
               li["anio"] = int(input("ingrese nuevo año de publicación"))
               li["genero"] =input("ingrese nuevo género")
            return
        print("libro no existe!")

def exportar_libro():
    if not libros:
        print("no existen libros, agrege uno")
    else:
        nombre_archivo = input("ingrese nombre del archivo: ")+".json"
        try:
            import json
            with open(nombre_archivo,"x") as archivo:
                json.dump(libros,archivo, indent=3)
                print("archivo creado!")
        except:
            print("ERROR, el nombre del archivo ya existe!")        
def salir():
    print("GRASIAS, A DIOS!")
    exit
#funcion extra:
def eliminar_libro():
    if not libros:
        print("no existen libros, favor de agregar libros!")
    else:
        print("\t eliminar libros") #se cambia el titulo al codigo de la opcion anterior 
        titulo_eliminar = input("ingrece el titulo del libro a eliminar")
        for li in libros:#li sería cada libro de la lista -> li: diccionario
            if titulo_eliminar.lower()==li["titulo"].lower() : # se busca el libro en la lista
               libros.remove(li)
               print("libro eliminado con exito")
               return
        print("libro no existe!")
    

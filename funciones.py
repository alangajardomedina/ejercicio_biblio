libros = []
#funciones
def agregar_libro():
    print("\t AGREGAR LIBRO")
    titulo=input("INgrese título:") 
    autor=input("INgrese autor:") 
    anio=input("INgrese año de publicación:") 
    genero=input("INgrese género:")
    libro={"titulo": titulo, "autor": autor, "anio":anio, "genero":genero}
    libros.append(libro)
    print("LIBRO AGREGADO!! :3") 
def mostrar_libros():
    if not libros:
        print("no existen libros, agregue uno porfavor")
    else:
        print("\t LISTA DE LIBROS")
        for li in libros: #li seria cada libro de la lista
            print("TITULO:", li["titulo"])
            print("AUTOR:", li["autor"])
            print("AÑO:", li["anio"])
            print("GÉNERO:", li["genero"])
            print("<3")

def buscar_libro():
    if not libros:
        print("no existen libros, agregue uno porfavor")
    else:
        print("\t BUSQUEDA DE LIBRO")
        titulo_buscar=input("INGRESE TITULO DEL LIBRO A BUSCAR: ")
        for li in libros: #li seria cada libro de la lista
            if titulo_buscar.lower()==li["titulo"].lower():
                print("AUTOR:", li["autor"])
                print("AÑO:", li["anio"])
                print("TITULO:", li["titulo"])
                print("GÉNERO:", li["genero"])
                break
    
def modificar_libro():

    if not libros:
        print("no existen libros, agregue uno porfavor")
    else:
        print("\t Modificar libro")
        titulo_modificar=input("INGRESE TITULO DEL LIBRO A modificar: ")
        for li in libros: #li seria cada libro de la lista
            if titulo_modificar.lower()==li["titulo"].lower():
                li["autor"]= input("ingrese nuevo autor: ")
                li["anio"]=int(input("ingrese nuevo anño de lanzamiento"))
                li["anio"]=int(input("ingrese nuevo anño de lanzamiento"))
                print("libro modificado!!!!! 8========)")
                break
def exportar_libro():
    if not libros:
        print("NO EXISTEN LIBROS, AGREGA UNO!!")
    else:
        nombre_archivo=input("INGRESE NOMBRE DEL ARCHIVO: ")+".json"
        try:
            import json
            with open(nombre_archivo,"x") as archivo:
                json.dump(libros, archivo, indent=2)
            print("ARCHIVO CREADOOOO!!!")
        except:
            print("ERROR, ARCHIVO YA Existe")
def salir():
    pass


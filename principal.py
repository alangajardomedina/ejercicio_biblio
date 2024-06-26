import time, os, json
from funciones import *

while True:
    os.system('cls')
    print("MENÚ BIBLIOTECA")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Buscar libro por títul")
    print("4. Modificar libro")
    print("5. Eliminar libro")
    print("6. Exportar a JSON")
    print("7. Salir")
    opc = int(input("Ingrese opción: "))
    os.system('cls')
    if opc==1:
        agregar_libro()
       
    elif opc==2:
        mostrar_libros()
    elif opc==3:
        buscar_libro()
    elif opc==4:
        modificar_libro()
    elif opc==5:
        eliminar_libro()
    elif opc==6:
        exportar_libro
    else:
        salir()
    time.sleep(3)
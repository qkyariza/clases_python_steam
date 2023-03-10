import os
from agregar_usuario import agregar_usuario
from actualizar_usuario import actualizar_usuario
from visualizar_usuario import visualizar_usuario
from eliminar_usuario import eliminar_usuario

base_dato = {}
os.system("cls")
print("\033[1m\nBienvenido a su sistema de gestion!\033[0m")

while True:
    def menu():
        print("\nQue deseas realizar: ")
        print("\t[1] - Para agregar usuario: ")
        print("\t[2] - Para actualizar usuario: ")
        print("\t[3] - Para visualizar todos los usuarios: ")
        print("\t[4] - Para visualizar usuario especifico: ")
        print("\t[5] - Para eliminar usuario: ")
        print("\t[6] - Para eliminar libro de ususario especifico: ")
        print("\t[0] - Para salir")
    
    menu()

    opcion = input("Favor ingresar opcion: ")
    match opcion:
        case "1":
            agregar_usuario(base_dato)
        case "2":
            actualizar_usuario(base_dato)
        case "3":
            print(base_dato)
        case "4":
            visualizar_usuario(base_dato)
        case "5":
            eliminar_usuario(base_dato)
        case "0":
            print("Programa finalizado!")
            break
        case _:
            print("Favor ingresar una opcion valida!")
    
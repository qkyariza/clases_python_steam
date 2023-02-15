import os
def agregar_usuario(
    z:dict
) -> dict:
    os.system("clear")
    name = input("Favor ingresar nombre: ")
    apellido = input("Favor ingresar apellido: ")
    book = input("Favor ingresar nombre del libro: ")
    z.update({name:book})
    os.system("clear")
    print(f"\033[1m\nSe ha agregado el usuario {name.capitalize()} con libro {book.capitalize()}\033[0m")

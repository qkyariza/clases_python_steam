
lista = []

usuario = input("Favod ingresar nombre de usuario: ")

def agregar(
    x:list
) -> list :
    x.append(usuario)
    print(x)

agregar(lista)

def eliminar(
    x:list
) -> list :
    x.remove(usuario)
    print(x)
eliminar(lista)


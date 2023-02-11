
def actualizar_usuario(
    z:dict
) -> dict:
    name = input("Favor ingresar nombre de usuario a ser actualizado: ")
    book = input("Favod ingresar nombre de nuevo libro: ")
    z[name] = book
    print(f"A usuario {name} actulizo a libro {book}")

def eliminar_usuario(
    z:dict
) -> dict:
    name = input("Favor ingresar nombre de usurio a eliminar: ")
    z.pop(name)
    print(f"Se ha eliminado usuario {name} con su registro!")

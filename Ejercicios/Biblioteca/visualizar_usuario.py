def visualizar_usuario(
    z:dict
) -> dict:
    name = input("Favor ingresar nombre a visualizar: ")
    print(f'El usuario {name} actualmente tiene el libro {z[name]}')

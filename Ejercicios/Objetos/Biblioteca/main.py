from objetos import Biblioteca

x = Biblioteca()

print("\033[1m\nBienvenido a su sistema de gestion!\033[0m")

while True:
    def menu():
        print("\nQue deseas realizar: ")
        print("\t[1] - Para agregar usuario: ")
        print("\t[2] - Para editar usuario: ")
        print("\t[3] - Para visualizar todos los usuarios: ")
        print("\t[4] - Para visualizar usuario especifico: ")
        print("\t[5] - Para eliminar usuario: ")
        print("\t[6] - Para eliminar libro de ususario especifico: ")
        print("\t[0] - Para salir")
    
    menu()

    opcion = input("Favor ingresar opcion a ejecutar: ")
    
    match opcion:
        case "1":
            x.Agregar()
        case "2":
            x.Editar()
        case "3":
            x.Visualizar()
     
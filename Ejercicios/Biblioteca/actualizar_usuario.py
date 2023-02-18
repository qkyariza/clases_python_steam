from datetime import datetime

def actualizar_usuario(z:dict) -> dict:
    name = input("\nFavor ingresar Nombre de usuario a ser actualizado: ")
    last_name = input("Favor ingresar Apellido de usuario a ser actualizado: ")
    nombre = name +" "+last_name
    date = datetime.now()
    date_date = date.strftime("%d %b %Y")
    date_time = date.strftime("%H:%M:%S")

    if nombre in z:
        book = input("Favor ingresar nombre de nuevo libro: ")
        
        diccionario_interno = {
            "\nNombre:":nombre,
            "Libro:":book,
            "Fecha:":date_date,
            "Hora:":date_time
        }

        z[nombre].append(diccionario_interno)
        for key,value in z.items():
            print(key + ": ")
            for book in value:
                for sub_key,sub_value in book.items():
                    print(f"{sub_key} {sub_value}")
                print()
        
        
        # print(f"\033[1m\n{z}\[0m")
    else:
        print("\033[1m\nUsuario no existente! Favor crear usuario en la opcion [1] - Agregar Usuario[0m")
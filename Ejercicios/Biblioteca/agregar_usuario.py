# {"felipe":[
    
#     {"libro":"habitos atomicos",
#     "fecha":"2023-02-14"},
    
#     {"libro":"Club 5 am",
#     "fecha":"2023-02-15"},
    
#     {"libro":"python completo",
#     "fecha":"2023-03-05"},
# ]}

from datetime import datetime

def agregar_usuario(z:dict) -> dict:
    name = input("Favor ingresar Nombre de usuario: ")
    last_name = input("Favor ingresar su Apellido: ")
    nombre = name + " " +last_name
    date = datetime.now()
    date_date = date.strftime("%d %b %Y")
    date_time = date.strftime("%H:%M:%S")

    if nombre in z:
        print("\n\033[1mUsuario exitente, por favor usar opcion [2] - Actualizar Usuario!\033[0m")
    else:
        book = input("Favor ingresar nombre del libro: ")
        
        diccionario_interno = {
            # "\nNombre:":nombre.title(),
            "\tLibro:":book.capitalize(),
            "\tFecha:":date_date,
            "\tHora:":date_time
            }

        z[nombre] = [diccionario_interno]
        print(f"\nLibros asociados a {nombre.title()}:")
        
        for key,value in diccionario_interno.items():
            print(key + ": " + str(value))
        
        # print(f"\033[1m\n{z}\033[0m")
        # print("\n\t".join("{} {}".format(a,j) for a,j in diccionario_interno.items()))
        

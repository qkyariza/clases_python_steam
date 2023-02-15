#Escriba una funcion que reciba una frase y devuelva un diccionario
#con las palabras que contiene y su longitud.

# def operacion_diccionario(
#     x:dict
# ) -> dict:
#     x = x.split(" ")
#     print(x)

#     diccionario = {}

#     for palabra in x:
#         diccionario[palabra] = len(palabra)
#     print(diccionario)

# operacion_diccionario("Hola como estas")

def operacion_diccionario(
    x:dict
) -> dict:
    x = x.split(" ")
    print(x)

    diccionario = {}

    for palabra in x:
        longitud = len(palabra)
        diccionario[palabra] = {
            "Longitud:":longitud
        }
    print(diccionario)
operacion_diccionario("Hola como estas?") 
    
lista_estudiantes = ["David","Omar","Isaac"]
lista_profesores = ["Felipe"]
lista_utensilios = ["PC","Maouse"]

def suma_lista(
    lista:list,
    lista2:list
) -> list :
    total = lista + lista2
    print(total)

suma_lista(lista_estudiantes,lista_profesores)

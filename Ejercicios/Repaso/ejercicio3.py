def funcion_ejemplo(a,b,c="Felipe"): #un valor predeterminado debe ir en la ultima posicion
    #logica
    d = int(input("Digita un numero: "))
    suma = a + b + d
    
    #retorno
    return suma

print(funcion_ejemplo(2,3))
#escriba un programa que permita crear dos lista de palabras y que, a continuacion, 
#elimine de la primera lista los nombres de la segunda lista.
#El programa debe preguntar por la cantidad de elementos en cada lista.

longitud_lista1 = int(input("Favor ingresar la longitud de la Lista 1: "))
lista1 = []

for i in range(longitud_lista1):
    elemento = input(f"Ingrese el elemento {i+1} de la primera lista: ")    
    lista1.append(elemento)
print(lista1)

longitud_lista2 = int(input("Favor ingresar la lingitud de la Lista 2: "))
lista2 = []

for j in range(longitud_lista2):
    elemento2 = input(f"Ingrese el elemento {j+1} de la segunda lista: ")
    lista2.append(elemento2)
print(lista2)

for k in lista2:
    if k in lista1:
        lista1.remove(k)

print("\nLista final es:", lista1)


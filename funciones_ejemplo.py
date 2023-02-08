def mayor_edad(edad:int) -> bool:
    if edad < 18:
        return 0
    else:
        return 1
e = int(input("Edad: "))
print(mayor_edad(e))
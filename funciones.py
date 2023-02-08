def area_rectangulo(
        x:float,
        y:float
) -> float:
    """
    Funcion que calcula el area de un rectangulo

    ---params---
    - x (float): es la base de mi rectangulo
    - y (float): es la altura de mi rectangulo

    ---return---
    - area (float): es el area de mi rectangulo
    """
    area = x*y
    return area

altura = float(input("Introdduce el area del rectangulo: "))
base = float(input("Introduce la base del triangulo: "))
result = area_rectangulo(base, altura)
print(f' El area del rectangulo es {result}')
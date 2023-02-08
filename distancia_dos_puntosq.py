import math

def distancia_dos_puntos(
    x1:float,
    x2:float,
    y1:float,
    y2:float
) -> float:
    """
        Funcion que calcula la distancia de dos puntos

        ---params---
        - x1 (float): posicion en x del punto 1
        - y1 (float): posicion en y del punto 1
        - x2 (float): posicion en x del punto 2
        - y2 (float): posicion en y del punto 2

        ---return---
        - distancia de dos puntos (float): es la distancia entre los dos puntos
        """
    x = math.pow(x2-x1,2)
    y = math.pow(y2-y1,2)
    d = math.sqrt(x+y)
    return d

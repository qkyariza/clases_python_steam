# class Robot():
#     x = input(int("Favor ingresar posicion en X inicial: "))
#     y = input(int("Favor ingresar posicion en Y inicial: "))

#     def __init__(self,nombre):
#         pass

#     def arriba():
#         pass

#     def abajo():
#         pass
    
#     def derecha():
#         pass

#     def izq():
#         pass

#     def posicion():
#         pass


# class Robot():
#     def __init__(self, nombre,x,y):
#         self.nombre = nombre
#         self.x = x
#         self.y = y

#     def arriba(self):
#         self.y += 1

#     def abajo(self):
#         self.y -= 1
    
#     def derecha(self):
#         self.x += 1

#     def izq(self):
#         self.x -= 1

#     def posicion(self):
#         print(f"La posición actual del robot {self.nombre} es: ({self.x}, {self.y})")

# # Ejemplo de uso
# robot1 = Robot("R2-D2", 0, 0)
# robot1.derecha()
# robot1.derecha()
# robot1.arriba()
# robot1.posicion()

# class Robot():
#     def __init__(self,nombre,x,y):
#         self.nombre = nombre
#         self.x = x
#         self.y = y

#     def mover(self,dx,dy):
#         self.x += dx
#         self.y += dy

#     def posicion(self):
#         print(f"La posición actual del robot {self.nombre} es: ({self.x}, {self.y})")


# # Pedir la posición inicial del robot al usuario
# nombre_robot = input("Ingrese el nombre del robot: ")
# x_inicial = int(input("Ingrese la posición inicial en X: "))
# y_inicial = int(input("Ingrese la posición inicial en Y: "))

# # Crear el objeto Robot con la posición inicial ingresada
# robot = Robot(nombre_robot,x_inicial,y_inicial)

# # Pedir al usuario cuántas posiciones quiere mover el robot en X e Y
# dx = int(input("Ingrese cuántas posiciones quiere mover el robot en X: "))
# dy = int(input("Ingrese cuántas posiciones quiere mover el robot en Y: "))

# # Mover el robot y mostrar la posición actual
# robot.mover(dx, dy)
# robot.posicion()

class Robot():

    def __init__(self,nombre,x,y):
        self.nombre = nombre
        self.x = x
        self.y = y
    
    def mov_horizontal(self,n):
        self.x = self.x + n

    def mov_vertical(self,n):
        self.y = self.y + n

    def posicion(self):
        print(f'{self.nombre} se encuentra en ({self.x},{self.y})')

robocito = Robot("Humberto",0,0)
robocito.mov_horizontal(3)
robocito.mov_vertical(4)
robocito.posicion()


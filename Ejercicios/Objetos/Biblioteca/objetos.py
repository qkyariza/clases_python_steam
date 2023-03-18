#Control bibliotecario: el bibliotecario lleva el control de prestar y devolucion libros
#Asignar, visualizar quien prestó, devolver el libro

#agregamos
from datetime import datetime
import os

class Biblioteca:
    os.system("cls")
    def __init__(self) -> None:
        self.biblioteca = {}
        
    def Agregar(self): 
        # self.datos = datos
        self.id = int(input('Ingresa tu cédula: '))
        self.nombre = input('Ingresa tu nombre: ')
        self.biblioteca[self.id] = self.nombre
        os.system("cls")
        print(f"Se agrego usuario: {self.biblioteca[self.id]}")
                
    def Editar (self):
        self.id = int(input('Ingrese el id de la persona: '))
        self.menu = int(input("""
            [1] - Agregar libro
            [2] - Editar estado de libro
            [3] - Elimar libro
        """))
        
        match self.menu:
            case 1:
                self.agregar_libro = input("Ingrese nombre de libro: ")
                date = datetime.now()
                self.fecha = date.strftime('%d %b %Y')
                self.hora = date.strftime("%H:%M:%S")
                diccionario_interno = {
                        'libro': self.agregar_libro,
                        'fecha': self.fecha,
                        'hora': self.hora,
                        'estado': 'Prestado'
                    }
                self.biblioteca[id] = diccionario_interno
                print (self.biblioteca)

    def Visualizar(self):
        print(self.biblioteca)
        
        
# {
#     'nombre':str,
#     'direccion':str,
#     'personas':{
#         'id':int,
#         'nombre':str,
#         'libros':[
#         {
#             'nombre':str,
#             'fecha':datetime,
#             'hora':datetime,
#             'estado':str
#         },
#         {
#             'nombre':str,
#             'fecha':datetime,
#             'hora':datetime,
#             'estado':str
#         },
#         ]
#     }
# }
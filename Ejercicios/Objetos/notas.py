#Realizar un programa que conste de una clase llamada Alumno que tenga como atributos
#el nimbre y la nota del alumno y definir los metodos para inicializar sus atributos, 
#imprimirlos y mostrar un mensaje con el resultado de la nota y #si ha aprobado o no.

class Alumno():


    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def aprobo(self):
        if self.nota 
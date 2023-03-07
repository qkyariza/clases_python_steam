class Coche():
    def __init__(self,matricula,marca,kilometros,gasolina):
        self.matricula = matricula
        self.marca = marca
        self.kilometros = kilometros
        self.gasolina = gasolina

    def avanzar(self,km):
        self.gasolina = self.gasolina - km
        self.kilometros = self.kilometros + km

david = Coche("QHY723","Chevrolet",45,20)
david.avanzar(25)

print(david.gasolina)
print(david.kilometros)

#completar: no puede quedar con lkilometros negativos
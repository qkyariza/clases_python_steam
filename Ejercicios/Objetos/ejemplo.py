class SerVivo():
    sentidos_listado = ["olfato","vista","olfato"]

    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        print(f"{self.nombre} esta haciendo un sonido")

    def movimiento(self):
        print(f"{self.nombre} se esta moviendo")

servivo = SerVivo("Guaka")
servivo.movimiento()
servivo.sonido()
print(servivo.sentidos_listado)

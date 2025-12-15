class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

class Coche(Vehiculo):
    def __init__(self, marca, puertas):
        super().__init__(marca)
        self.puertas = puertas

    def info(self):
        print("El coche es un", self.marca, "y tiene", self.puertas, "puertas")

class Camion(Vehiculo):
    def __init__(self, marca, ruedas):
        super().__init__(marca)
        self.ruedas = ruedas

    def info(self):
        print("El camion es un", self.marca, "y tiene", self.ruedas, "ruedas")

coche = Coche("Dacia Sandero", 5)
coche.info()

camion = Camion("Mercedes-Benz Actros", 8)
camion.info()
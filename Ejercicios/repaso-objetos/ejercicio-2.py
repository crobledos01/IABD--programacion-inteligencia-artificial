class Coche:
    def __init__(self, marca, modelo, ano, color):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.color = color

def mostrar_atributos(coche):
    print("Marca:", coche.marca)
    print("Modelo:", coche.modelo)
    print("Año:", coche.ano)
    print("Color:", coche.color)

coche = Coche("Seat", "Arona", 2014, "Rojo")
mostrar_atributos(coche)
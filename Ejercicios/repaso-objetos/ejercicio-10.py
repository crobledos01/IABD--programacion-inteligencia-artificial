class Figura:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        print("El área de la figura es:", self.base * self.altura)

class Circulo(Figura):
    def __init__(self, base, altura, radio):
        super().__init__(base, altura)
        self.radio = radio

    def calcular_area(self):
        print("El área del círculo es:", self.radio ** 2 * 3.14, "cm cuadrados")

class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__(base, altura)

    def calcular_area(self):
        print("El área del rectángulo es:", self.base * self.altura, "cm cuadrados")

radio = int(input("Introduce el radio del círculo en centímetros: "))
circulo = Circulo(0, 0, radio)
circulo.calcular_area()

base = int(input("Introduce la base del rectángulo en centímetros: "))
altura = int(input("Introduce la altura del rectángulo en centímetros: "))
rectangulo = Rectangulo(base, altura)
rectangulo.calcular_area()
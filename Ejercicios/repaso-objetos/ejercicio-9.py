class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_bonus(self):
        print("El bonus que corresponde a", self.nombre, "según su salario son", self.salario * 0.1, "€")

class Vendedor(Empleado):
    def __init__(self, nombre, salario, ventas):
        super().__init__(nombre, salario)
        self.ventas = ventas

    def calcular_bonus(self):
        print("El bonus que corresponde a", self.nombre, "según las ventas realizadas son", self.ventas * 0.1, "€")

nombre = input("Introduce el nombre del empleado: ")
salario = int(input("Introduce el salario del empleado: "))
ventas = int(input("Introduce el dinero en ventas del empleado: "))

vendedor = Vendedor(nombre, salario, ventas)
vendedor.calcular_bonus()

#Se crea una clase empleado y se le añaden sus variables. Después, se calcula el bonus en base a su salario
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_bonus(self):
        print("El bonus que corresponde a", self.nombre, "según su salario son", self.salario * 0.1, "€")

#Se crea la sublcase vendedor que proviene de empleado, se añade ventas a la información ya existente.
#Después, se actualiza calcular_bonus para que utilice las ventas en lugar del salario
class Vendedor(Empleado):
    def __init__(self, nombre, salario, ventas):
        super().__init__(nombre, salario)
        self.ventas = ventas

    def calcular_bonus(self):
        print("El bonus que corresponde a", self.nombre, "según las ventas realizadas son", self.ventas * 0.1, "€")

#Se piden al usuario los valores del vendedor
nombre = input("Introduce el nombre del empleado: ")
salario = int(input("Introduce el salario del empleado: "))
ventas = int(input("Introduce el dinero en ventas del empleado: "))

#Se crea el vendedor y se llama a su función de calcular bonus
vendedor = Vendedor(nombre, salario, ventas)
vendedor.calcular_bonus()

class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

class Gerente(Empleado):
    def __init__(self, nombre, puesto, salario, departamento):
        super().__init__(nombre, puesto, salario)
        self.departamento = departamento

    def informar(self):
        print("El empleado", self.nombre, "con puesto", self.puesto, "en el departamento de", self.departamento, "tiene un salario de", self.salario, "€")

gerente = Gerente("Juan", "UX/UI", 1500, "informática")

gerente.informar()
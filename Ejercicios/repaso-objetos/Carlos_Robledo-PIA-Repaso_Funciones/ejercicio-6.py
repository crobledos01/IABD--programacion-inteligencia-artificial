#Crear la clase empleado con las 3 variables
class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

#Se crea la subclase Gerente y se le pasa empleado, se añaden las 3 variables anteriores usando super y la nueva variable departamento
#Dentro de la clase, se añade una función informar que muestra en pantalla tanto el departamento como los datos procedentes de empleado
class Gerente(Empleado):
    def __init__(self, nombre, puesto, salario, departamento):
        super().__init__(nombre, puesto, salario)
        self.departamento = departamento

    def informar(self):
        print("El empleado", self.nombre, "con puesto", self.puesto, "en el departamento de", self.departamento, "tiene un salario de", self.salario, "€")

#Se añade un gerente con la información necesaria y se llama a la función informar que contiene
gerente = Gerente("Juan", "UX/UI", 1500, "informática")
gerente.informar()
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
if numero1 > numero2:
    resultado = "mayor"
elif numero1 < numero2:
    resultado = "menor"
else:
    resultado = "igual" 

print("El primer número es", resultado, "que el segundo")
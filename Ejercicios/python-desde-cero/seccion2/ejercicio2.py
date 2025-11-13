numero = int(input("Introduce un número: "))
if numero > 0:
    resultado = "mayor"
elif numero < 0:
    resultado = "menor"
else:
    resultado = "igual" 

print("El número es", resultado, "que 0")
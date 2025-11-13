caracter = input("Introduce un carácter: ")
if caracter.isupper():
    resultado = "mayúscula"
elif caracter.islower():
    resultado = "minúscula"
else:
    resultado = "distinto a una letra"
print("El carácter es ", resultado)
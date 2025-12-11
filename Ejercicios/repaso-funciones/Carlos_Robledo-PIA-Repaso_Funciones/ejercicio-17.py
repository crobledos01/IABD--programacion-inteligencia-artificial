#Se pide al usuario que introduzca el texto
texto = input("Introduce un texto: ")

#Se crea una segunda variable vacía a la que se le van añadiendo los caracteres del texto al principio de la cadena
invertido = ""
for c in texto:
    invertido = c + invertido

#Compara ambos textos, si son iguales es un palíndromo
if texto == invertido:
    print(f"El texto '{texto}' es un palíndromo")
else:
    print(f"El texto '{texto}' no es un palíndromo")
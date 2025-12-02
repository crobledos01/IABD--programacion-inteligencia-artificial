texto = input("Introduce un texto: ")
invertido = ""

for c in texto:
    invertido = c + invertido

if texto == invertido:
    print(f"El texto '{texto}' es un palíndromo")
else:
    print(f"El texto '{texto}' no es un palíndromo")
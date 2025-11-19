cadena = input("Introduce una palabra o una frase: ")
diccionario = {}
for caracter in cadena:
    if caracter.capitalize() in diccionario and caracter != " ":
        diccionario[caracter.capitalize()] += 1
    elif caracter != " ":
        diccionario[caracter.capitalize()] = 1

for palabra, cantidad in diccionario.items():
    print(palabra, ":", cantidad)
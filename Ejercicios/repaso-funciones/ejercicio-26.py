def contar_caracteres(char, cadena):
    return cadena.count(char)

cadena = input("Introduce una cadena: ")
char = input("Introduce un caracter: ")

print("El caracter", char, "aparece en la cadena", contar_caracteres(char, cadena), "veces")
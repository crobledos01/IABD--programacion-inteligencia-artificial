import cadenas

# Se le pide al usuario que introduzca un texto
texto = input("Introduce un texto: ")

# Imprime los resultados de las funciones del módulo cadenas
print("Cadena invertida:", cadenas.invertir(texto))
print("Número de vocales:", cadenas.contar_vocales(texto))
print("Mayúsculas:", cadenas.a_mayusculas(texto))
print("Minúsculas:", cadenas.a_minusculas(texto))
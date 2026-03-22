# Esta función devuelve la cadena invertida
def invertir(cadena):
    return cadena[::-1]

# Esta función cuenta el número de vocales en la cadena
## Para ello, crea una cadena con las vocales, genera un contador y convierte la cadena a minúsculas
## Por último, recorre cada letra de la cadena e incrementa el contador si la letra es una bocal
def contar_vocales(cadena):
    vocales = "aeiou"
    contador = 0
    cadena = cadena.lower()
    for letra in cadena:
        if letra in vocales:
            contador += 1
            
    return contador

# Esta función convierte la cadena a mayúsculas
def a_mayusculas(cadena):
    return cadena.upper()

# Esta función convierte la cadena a minúsculas
def a_minusculas(cadena):
    return cadena.lower()
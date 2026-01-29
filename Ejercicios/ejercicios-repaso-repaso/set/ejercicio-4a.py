# Se importa un string que contiene todas las letras del abecedario latino, al que se le suma la ñ a mano
from string import ascii_lowercase as asc_lower
asc_lower = asc_lower + 'ñ'
# Se pide al usuario una cadena de texto y se quitan los espacios
cadena = input("Introduce una cadena de texto: ")
cadena_sin_espacios = cadena.replace(" ", "")
# Se crea un set que contenga todas las letras del abecedario
set_caracteres = set(asc_lower)
# Se recorre la cadena letra por letra y se descarta en el set, si no existe de antemano no ocurre ningún error
for c in cadena_sin_espacios:
    set_caracteres.discard(c)
    # Si el set está vacío, es que es un pangrama, si contiene alguna letra no lo es
if len(set_caracteres) == 0:
    print("La cadena es un pangrama")
else:
    print("La cadena NO es un pangrama")
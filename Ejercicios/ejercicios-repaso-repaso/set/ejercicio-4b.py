# Se importa un string que contiene todas las letras del abecedario latino, al que se le suma la ñ a mano
from string import ascii_lowercase as asc_lower
asc_lower = asc_lower + 'ñ'
# Se pide al usuario una cadena de texto y se quitan los espacios
cadena = input("Introduce una cadena de texto: ")
cadena_sin_espacios = cadena.replace(" ", "")
# Se crea un set vacío
set_caracteres = set()
# Se recorre la cadena letra por letra y se añade al set, si ya existe de antemano no se duplica
for c in cadena_sin_espacios:
    set_caracteres.add(c)
# Si el set contiene la misma cantidad de elementos que el abecedario, es un pangrama
if len(asc_lower) == len(set_caracteres):
    print("La cadena es un pangrama")
else:
    print("La cadena NO es un pangrama")
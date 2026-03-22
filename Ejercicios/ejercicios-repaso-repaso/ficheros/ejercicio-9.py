from collections import defaultdict
from pathlib import Path
import sys

# Esta función carga el diccionario de palabras en un indice donde se incluye una palabra y su firma, que actua como clave
# La clave es un texto con las letras de la palabra ordenadas alfabéticamente, que servirá para encontrar anagramas
def cargar_diccionario(ruta):
    # Busca el archivo en la ruta dada y, si no lo encuentra, lanza un error
    indice = defaultdict(list)
    ruta = Path(ruta)
    if not ruta.is_file():
        raise FileNotFoundError(f"Archivo no encontrado: {ruta}")

    # Lee el archivo línea por línea y por cada línea obtiene las palabras, calcula su firma y las añade al indice
    with ruta.open(encoding="utf-8") as f:
        for linea in f:
            palabras = linea.strip().lower()
            for palabra in palabras.split():
                firma = "".join(sorted(palabra))
                indice[firma].append(palabra)

    return indice

# Esta función busca los anagramas de una palabra dada, utilizando el indice del diccionario
def buscar_anagramas(palabra, diccionario):
    # Primero, la palabra del usuario se pasa a minúsculas y se calcula la firma de la palabra
    palabra = palabra.lower()
    firma = "".join(sorted(palabra))

    # Obtiene todas las palabras que contienen la misma firma que la palabra del usuario
    posibles = diccionario.get(firma, [])

    # Devuelve todas las palabras posibles, dejando fuera la palabra original
    return sorted(w for w in posibles if w != palabra)

# He tenido que añadir el script y el path porque si no, el programa no encuentra el archivo
ruta_dic = "diccionario_castellano.txt"
script_dir = Path(__file__).parent
ruta_path = Path(ruta_dic)

if not ruta_path.is_file():
    ruta_path = script_dir / ruta_dic

try:
    diccionario = cargar_diccionario(ruta_path)
except FileNotFoundError:
    print(f"Error: no se encontró '{ruta_dic}'. Coloca el archivo en {script_dir} o especifica la ruta.")
    sys.exit(1)

# Se pide al usuario que introduzca una palabra, se buscan sus anagramas y se muestran por pantalla
palabra = input("Introduce una palabra: ").strip().lower()
anagramas = buscar_anagramas(palabra, diccionario)
if anagramas:
    print(f"\nAnagramas encontrados para '{palabra}':")
    for a in anagramas:
        print(a)
else:
    print(f"\nNo se encontraron anagramas para '{palabra}'.")
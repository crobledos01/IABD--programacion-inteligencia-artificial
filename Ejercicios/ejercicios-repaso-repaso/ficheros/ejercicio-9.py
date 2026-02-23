from itertools import permutations

def cargar_diccionario(ruta_dic: str) -> set:
    with open(ruta_dic, encoding="utf-8") as f:
        return {linea.strip().lower() for linea in f if linea.strip()}

def generar_anagramas(palabra: str, diccionario: set) -> list:
    palabra = palabra.lower()
    anagramas = set()

    for perm in set(permutations(palabra)):
        candidata = "".join(perm)
        if candidata != palabra and candidata in diccionario:
            anagramas.add(candidata)

    return sorted(anagramas)

def procesar_anagramas(
    ruta_palabras: str,
    ruta_dic: str,
    ruta_salida: str = "listaanagramas.txt",
) -> None:
    diccionario = cargar_diccionario(ruta_dic)

    with open(ruta_palabras, encoding="utf-8") as f_in, \
         open(ruta_salida, "w", encoding="utf-8") as f_out:
        for linea in f_in:
            palabra = linea.strip()
            if not palabra:
                continue
            anags = generar_anagramas(palabra, diccionario)
            if anags:
                f_out.write(f"{palabra} {', '.join(anags)}\n")
            else:
                f_out.write(f"{palabra}\n")

import argparse

ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Función para convertir el texto a mayúsculas y eliminar espacios
def normalizar(txt):
    return txt.upper().replace(" ", "")

# Función para generar la clave final a través de la orginal
## Esta función comprueba que la clave no esté vacía
## En caso de que no lo esté, devuelve la clave repetida la cantidad de veces necesaria para que tenga la longitud del texto
def generar_clave(texto, clave):
    clave = normalizar(clave)
    if not clave:
        raise ValueError("No existe clave")
    resultado = (clave * ((len(texto) // len(clave)) + 1))[:len(texto)]
    return resultado

# Función para cifrar el mensaje utilizando la clave
## Primero, normaliza el mensaje, genera la clave y crea una lista vacía para guardar el resultado
## Luego, recorre cada letra del mensaje y la clave, calcula el índice de la letra y lo suma al resultado
## Por último, utiliza join para unir las letras de la lista y lo devuelve
def cifrar(mensaje, clave):
    mensaje = normalizar(mensaje)
    clave = generar_clave(mensaje, clave)
    resultado = []

    for m, c in zip(mensaje, clave):
        id = (ALFABETO.index(m) + ALFABETO.index(c)) % len(ALFABETO)
        resultado.append(ALFABETO[id])

    return "".join(resultado)

# Función para cifrar el mensaje utilizando la clave
## Primero, normaliza el mensaje, genera la clave y crea una lista vacía para guardar el resultado
## Luego, recorre cada letra del mensaje y la clave, calcula el índice de la letra y lo resta al resultado
## Por último, utiliza join para unir las letras de la lista y lo devuelve
def descifrar(mensaje: str, clave: str) -> str:
    mensaje = normalizar(mensaje)
    clave = generar_clave(mensaje, clave)
    resultado = []

    for m, c in zip(mensaje, clave):
        id = (ALFABETO.index(m) - ALFABETO.index(c)) % len(ALFABETO)
        resultado.append(ALFABETO[id])

    return "".join(resultado)

# Función para convertir los argumentos de la línea de comandos
## Esta función utiliza argparse para definir los argumentos que se pueden pasar al programa
def parse_args():
    parser = argparse.ArgumentParser(
        "cifrado",
        description="Cifrado/descifrado vigenere con alfabeto castellano",
        epilog="python cifrado.py -c PROGRAMACIONDEIA -k covid",
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-c", "--cifrar",
        help="Mensaje a cifrar",
        type=str,
    )
    group.add_argument(
        "-d", "--descifrar",
        help="Mensaje a descifrar",
        type=str,
    )

    parser.add_argument(
        "-k", "--key",
        help="Palabra clave para el cifrado/descifrado",
        required=True,
        type=str,
    )

    return parser.parse_args()

# Función principal del programa
## Primero, utiliza args para obtener los argumentos de la línea de comandos
## Luego, comprueba si se ha pasado el argumento de cifrar o descifrar y llama a la función correspondiente
## Por último, imprime el texto original, la clave y el resultado en la consola
def main():
    args = parse_args()

    if args.cifrar:
        texto = args.cifrar
        resultado = cifrar(texto, args.key)
        print(f"Texto original : {texto}")
        print(f"Clave          : {args.key}")
        print(f"Texto cifrado  : {resultado}")
    elif args.descifrar:
        texto = args.descifrar
        resultado = descifrar(texto, args.key)
        print(f"Texto cifrado    : {texto}")
        print(f"Clave            : {args.key}")
        print(f"Texto descifrado : {resultado}")

# Punto de entrada del programa
if __name__ == "__main__":
    main()

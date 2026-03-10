import argparse

ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
LONG_ALFABETO = len(ALFABETO)


def generar_clave(mensaje, clave):
    clave = clave.upper()
    clave_repetida = ""

    for i in range(len(mensaje)):
        clave_repetida += clave[i % len(clave)]

    return clave_repetida


def cifrar_vigenere(mensaje, clave):
    mensaje = mensaje.upper()
    clave = generar_clave(mensaje, clave)
    resultado = ""

    for m, k in zip(mensaje, clave):
        pos_m = ALFABETO.index(m)
        pos_k = ALFABETO.index(k)

        nueva_pos = (pos_m + pos_k) % LONG_ALFABETO
        resultado += ALFABETO[nueva_pos]

    return resultado


def descifrar_vigenere(mensaje, clave):
    mensaje = mensaje.upper()
    clave = generar_clave(mensaje, clave)
    resultado = ""

    for m, k in zip(mensaje, clave):
        pos_m = ALFABETO.index(m)
        pos_k = ALFABETO.index(k)

        nueva_pos = (pos_m - pos_k) % LONG_ALFABETO
        resultado += ALFABETO[nueva_pos]

    return resultado


def main():
    parser = argparse.ArgumentParser(
        description="Cifrado y descifrado Vigenere",
        epilog="Ejemplo: python cifrado_vigenere.py -c MENSAJE -k CLAVE"
    )

    grupo = parser.add_mutually_exclusive_group(required=True)

    grupo.add_argument("-c", "--cifrar", help="Mensaje a cifrar")
    grupo.add_argument("-d", "--descifrar", help="Mensaje a descifrar")

    parser.add_argument("-k", "--clave", help="Clave de cifrado", required=True)

    args = parser.parse_args()

    if args.cifrar:
        resultado = cifrar_vigenere(args.cifrar, args.clave)
        print("Mensaje cifrado:", resultado)

    elif args.descifrar:
        resultado = descifrar_vigenere(args.descifrar, args.clave)
        print("Mensaje descifrado:", resultado)


if __name__ == "__main__":
    main()
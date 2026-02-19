# Busca la palabra con mayor puntuación en una frase, sumando el valor de cada letra (a=1, b=2, ...)
def palabra_mayor_valor(frase):
    letras = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m', 'n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'
    ]
    # Separa la frase en palabras
    palabras = frase.split()
    max_puntuacion = 0
    mejor_palabra = ""

    # Calcula la puntuación de cada palabra
    for palabra in palabras:
        puntuacion = 0
        for letra in palabra:
            if letra in letras:
                puntuacion += letras.index(letra) + 1
        # Si la puntuación es mayor que la máxima, actualiza
        if puntuacion > max_puntuacion:
            max_puntuacion = puntuacion
            mejor_palabra = palabra

    return mejor_palabra

# Solicita una frase al usuario y muestra la palabra con mayor puntuación
frase = input("Introduce una frase: ")
palabra = palabra_mayor_valor(frase.lower())
print(f"La palabra con mejor puntuacion es {palabra}")
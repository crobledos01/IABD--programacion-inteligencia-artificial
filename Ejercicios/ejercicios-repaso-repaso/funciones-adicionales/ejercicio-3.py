def palabra_mayor_valor(frase):
    letras = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m', 'n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'
    ]
    
    palabras = frase.split()
    max_puntaje = 0
    mejor_palabra = ""

    for palabra in palabras:
        puntaje = 0
        for letra in palabra:
            if letra in letras:
                puntaje += letras.index(letra) + 1
        
        if puntaje > max_puntaje:
            max_puntaje = puntaje
            mejor_palabra = palabra

    return mejor_palabra

frase = input("Introduce una frase: ")
palabra = palabra_mayor_valor(frase.upper())
print(f"La palabra con mejor puntaje es {palabra}")
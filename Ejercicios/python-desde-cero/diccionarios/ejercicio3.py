def quitar_tildes(texto):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for tilde, simple in replacements:
        texto = texto.replace(tilde, simple).replace(tilde.lower(), simple.lower())
    return texto

precio_frutas = {
    "manzana": 0.5,
    "platano": 0.3,
    "cereza": 0.2,
    "durazno": 0.4,
    "pera": 0.6
}

continuar = True
while continuar == True:
    fruta = quitar_tildes(input("Introduce la fruta: ")).lower()
    if(fruta in precio_frutas):
        cantidad = int(input("Introduce la cantidad: "))
        print("El precio total es:", cantidad * precio_frutas[fruta], "€")
    else:
        print("La fruta introducida NO es válida.")

    salir = input("Pulsa * para salir o cualquier otra tecla para añadir otra fruta: ")
    if salir == "*":
        continuar = False



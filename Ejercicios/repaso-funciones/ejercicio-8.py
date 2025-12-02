texto = input("Introduce una cadena de texto: ")
texto = texto.lower()
vocales = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}
for c in texto:
    if c in vocales:
        vocales[c] = vocales[c] + 1

for vocal in vocales:
    print("La vocal", vocal, "aparece", vocales[vocal])
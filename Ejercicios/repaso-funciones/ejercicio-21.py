def convertir_binario(binario):
    
    decimal = 0
    for index, v in enumerate(binario):
        if v == "1":
            decimal = decimal + (2 ** (len(binario) - (index + 1)))

    return decimal

binario = input("Introduce un número binario: ")

print("Tu número en decimal es:", convertir_binario(binario))
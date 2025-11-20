def EsMultiplo(mayor, menor):
    return (mayor % menor == 0)

numeros = []

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

numeros.append(numero1)
numeros.append(numero2)

numeros.sort(reverse=True)

if(EsMultiplo(numeros[0], numeros[1])):
    print("El número", numeros[0], "es múltiplo de", numeros[1])
else:
    print("Los números no son primos")
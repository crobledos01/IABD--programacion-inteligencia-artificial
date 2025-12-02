def esMenor(valor, input):
    if valor < input:
        return True
    else:
        return False

numero = int(input("Introduce un número: "))
anterior = 0
ultimo = 1
continuar = True
print("Los números en la cadena de Fibonacci menores que", numero, "son:")
while continuar:
    total = anterior + ultimo
    if(esMenor(total, numero)):
        copia_ultimo = ultimo
        print(total, end=", ")
        ultimo = total
        anterior = copia_ultimo
    else:
        continuar = False

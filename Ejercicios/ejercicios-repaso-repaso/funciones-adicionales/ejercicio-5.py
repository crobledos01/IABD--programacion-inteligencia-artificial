# Encuentra el número atípico (par o impar) en una lista donde todos menos uno son del mismo tipo
def encontrar_atipico(lista):
    # Convierte la cadena en una lista de enteros
    numeros = [int(n.strip()) for n in lista.split(",")]

    # Cuenta cuántos pares hay en los tres primeros números
    pares = [n for n in numeros[:3] if n % 2 == 0]

    # Si la mayoría son pares, busca el impar; si no, busca el par
    if len(pares) >= 2:
        for num in numeros:
            if num % 2 != 0:
                return num
    else:
        for num in numeros:
            if num % 2 == 0:
                return num

# Solicita la lista al usuario y muestra el número atípico
lista = input("Introduce una lista de números separados solo por comas: ")
print("El número atípico es:", encontrar_atipico(lista))

def calcDivisores(numero):
    divisores = []
    i = 1
    while i <= numero / 2:
        if numero % i == 0:
            divisores.append(i)
        i += 1
    return divisores

def buscar_numeros_amigos(cantidad):
    num_busquedas = 10000
    numeros_amigos = []

    while len(numeros_amigos) < cantidad:
        numeros_amigos = []
        suma_divisores = [0] * num_busquedas
        for n in range(0, num_busquedas // 2 + 1):
            divisores = calcDivisores(n)
            suma_divisores[n] = sum(divisores)
        
        for n in range(0, num_busquedas // 2 + 1):
            divisores = calcDivisores(n)
            sum_div = sum(divisores)
            for m in range(0, num_busquedas // 2 + 1):
                if n > m and n != m and suma_divisores[m] == n and sum_div == m:
                    numeros_amigos.append((m, n))

        num_busquedas = num_busquedas + 10000

    return numeros_amigos[:cantidad]

cantidad = int(input("Introduce la cantidad de números amigos a encontrar: "))
lista_na = buscar_numeros_amigos(cantidad)

print(f"Los primeras {cantidad} parejas de números amigos son: {lista_na}")
def primeras_parejas_amigos(x):

    #Realiza 
    N = 10000
    numeros_amigos = []

    while len(numeros_amigos) < x:
        # Inicializamos la suma de divisores
        suma_divisores = [0] * (N + 1)

        # Llenamos la suma de divisores propios
        for d in range(1, N // 2 + 1):
            for m in range(2*d, N + 1, d):
                suma_divisores[m] += d

        # Buscamos parejas de números amigos
        numeros_amigos.clear()  # Limpiamos por si necesitamos repetir con N más grande
        for n in range(2, N + 1):
            m = suma_divisores[n]
            if m > n and m <= N and suma_divisores[m] == n:
                numeros_amigos.append((n, m))
        
        if len(numeros_amigos) < x:
            # Si no encontramos suficientes, aumentamos el rango
            N *= 2

    # Devolvemos solo las primeras x parejas
    return numeros_amigos[:x]

numero = int(input("Introduce la cantidad de números amigos: "))
for a, b in primeras_parejas_amigos(numero):
    print(a, b)

import ejercicio_1_modulo as modulo

# Llamando a las funciones del módulo, se generan números aleatorios, se imprimen, se ordenan y se vuelven a imprimir
numeros = modulo.generar_numeros_aleatorios()
print("Números generados:")
modulo.imprimir_numeros(numeros)
numeros_ordenados = modulo.ordenar_numeros(numeros)
print("Números ordenados:")
modulo.imprimir_numeros(numeros_ordenados)
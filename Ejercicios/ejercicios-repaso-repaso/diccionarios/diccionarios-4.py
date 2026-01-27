#Datos de pruebas:
datos_ventas = {
    'Norte': [
        ('Producto1', 27, 13.79),
        ('Producto5', 2, 31.87),
        ('Producto5', 3, 74.2),
        ('Producto5', 43, 80.26),
        ('Producto2', 23, 74.13),
        ('Producto2', 29, 49.84)
    ],
    'Sur': [
        ('Producto2', 15, 44.02),
        ('Producto5', 12, 90.66),
        ('Producto1', 33, 18.45),
        ('Producto5', 1, 88.74),
        ('Producto5', 16, 15.71),
        ('Producto3', 49, 94.61),
        ('Producto1', 12, 45.9),
        ('Producto1', 17, 87.96),
        ('Producto3', 36, 50.98),
        ('Producto4', 18, 39.32)
    ],
    'Este': [
        ('Producto3', 43, 95.86),
        ('Producto4', 8, 65.2),
        ('Producto5', 8, 72.66),
        ('Producto2', 12, 73.69),
        ('Producto5', 3, 46.67),
        ('Producto5', 1, 85.29),
        ('Producto5', 21, 94.97),
        ('Producto3', 45, 92.51),
        ('Producto3', 50, 79.64),
        ('Producto3', 4, 24.18)
    ],
    'Oeste': [
        ('Producto3', 6, 14.02),
        ('Producto3', 47, 21.55),
        ('Producto4', 46, 32.02),
        ('Producto3', 45, 46.97),
        ('Producto5', 2, 30.75)
    ],
    'Centro': [
        ('Producto4', 41, 21.6),
        ('Producto3', 20, 64.34),
        ('Producto1', 36, 36.65),
        ('Producto3', 39, 17.97),
        ('Producto5', 8, 67.43),
        ('Producto2', 35, 11.5)
    ]
}
# Se crea un diccionario para guardar los resultados
ingresos_por_region = {}
# Se utiliza un bucle que saca por un lado el nombre de cada región del diccionario original y por otro sus valores
for region, ventas in datos_ventas.items():
    # Se crea una variable para ver las ventas por region
    total_ventas = 0
    # Se realiza un nuevo bucle que saca el nombre del producto (no interesa), el precio y la cantidad de la lista de ventas por región
    # Dentro, se multiplican las cantidades por el precio de cada producto y se suma a la variable de ventas
    for _, cantidad, precio in ventas:
        total_ventas = total_ventas + cantidad * precio
    # Por cada región se añade un nuevo apartado en el nuevo diccionario y se meten los ingresos por región redondeados
    ingresos_por_region[region] = round(total_ventas, 2)
# Imprime el ingreso total por región
print("El ingreso total por región es: ")
print(ingresos_por_region)

import ejercicio_2_modulo as modulo

# Se pide al usuario el total de la compra
total = float(input("Introduce el total de la compra: "))
# Se llama a la función para comprobar si el descuento es aplicable
if modulo.descuento_aplicable(total):
    # En caso de que el descuento sea aplicable, se selecciona una bola y se calcula el descuento
    bola = modulo.seleccionar_bola()
    modulo.calcular_descuento(total, bola)
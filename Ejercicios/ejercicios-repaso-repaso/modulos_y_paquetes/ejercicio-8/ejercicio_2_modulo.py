import random

# Esta función comprueba si el total es mayor o igual a 100
## En caso negativo, se informa al usuario y se devuelve False para indicar que no se puede aplicar el descuento
## En caso positivo, se devuelve True para indicar que se puede aplicar el descuento
def descuento_aplicable(total):
    tirada_bola = total >= 100
    if not tirada_bola:
        print("No hay promoción aplicable, el total es menor a 100€")
    return tirada_bola

# Esta función selecciona una bola al azar entre las disponibles y devuelve su color
def seleccionar_bola():
    bolas = ["blanca", "roja", "azul", "verde", "amarilla"]
    return random.choice(bolas)

# Esta función calcula el descuento aplicable según el color de la bola seleccionada
## Se utiliza un match-case para asignar el porcentaje de descuento correspondiente a cada color de bola
## Tras esto, se muestra el color de la bola, el descuento aplicado y el total final a pagar
def calcular_descuento(total, bola):

    match bola:
        case "roja": descuento = 0.10
        case "azul": descuento = 0.20
        case "verde": descuento = 0.25
        case "amarilla": descuento = 0.50
        case _: descuento = 0.0
        
    print(f"Has sacado la bola {bola}, por lo que tienes un descuento del {descuento*100:.0f}%")
    total_final = total * (1 - descuento)
    print(f"El total a pagar es: {total_final:.2f}€")
x1 = int(input("Introduce el punto x1: "))
y1 = int(input("Introduce el punto y1: "))
x2 = int(input("Introduce el punto x2: "))
y2 = int(input("Introduce el punto y2: "))
r1 = int(input("Introduce el radio del círculo 1: "))
r2 = int(input("Introduce el radio del círculo 2: "))
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
if distancia == r1 + r2:
    print("Los círculos son secantes")
elif distancia > r1 + r2:
    print("Los círculos son exteriores")
else:
    if distancia + min(r1, r2) < max(r1, r2):
        print("Los círculos son interiores")
    else:
        print("Los círculos son tangentes interiores")
if x1 == x2 and y1 == y2:
    print("Los círculos son concéntricos")
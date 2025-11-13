import math

x1 = int(input("Introduce la coordenada x del primer punto: "))
y1 = int(input("Introduce la coordenada y del primer punto: "))
x2 = int(input("Introduce la coordenada x del segundo punto: "))
y2 = int(input("Introduce la coordenada y del segundo punto: "))
distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("La distancia entre los dos puntos es:", distancia)
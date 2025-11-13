distancia = int(input("Introduce la distancia entre los vehículos en km: "))
velocidad1 = int(input("Introduce la velocidad del primer vehículo (km/h): "))
velocidad2 = int(input("Introduce la velocidad del segundo vehículo (km/h): "))
if velocidad1 > velocidad2:
    tiempo = (distancia / (velocidad1 - velocidad2)) * 60
else:
    tiempo = (distancia / (velocidad2 - velocidad1)) * 60
print("El tiempo hasta que se encuentren los dos vehículos es:", tiempo , "minutos")
hora_salida = int(input("Introduce la hora de salida: "))
minuto_salida = int(input("Introduce el minuto de salida: "))
segundo_salida = int(input("Introduce el segundo de salida: "))
distancia = int(input("Introduce la distancia hasta el destino en segundos: "))
horas_de_distancia = int(distancia / 3600)
minutos_de_distancia = int((distancia / 60) - (horas_de_distancia * 60))
segundos_de_distancia = distancia % 60
total_horas = hora_salida + horas_de_distancia
total_minutos = minuto_salida + minutos_de_distancia
total_segundos = segundo_salida + segundos_de_distancia
if total_segundos > 60:
    segundo_llegada = total_segundos % 60
    total_minutos += 1
else:
    segundo_llegada = total_segundos
if total_minutos > 60:
    minuto_llegada = total_minutos % 60
    total_horas += 1
else:
    minuto_llegada = total_minutos
if total_horas > 23:
    hora_llegada = total_horas % 24
else:
    hora_llegada = total_horas
print("La hora de llegada será las", hora_llegada, "horas,", minuto_llegada, "minutos,", segundo_llegada, "segundos")
dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))
dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if año % 4 == 2:
    dias_por_mes[1] = 29
try:
    if (dias_por_mes[mes - 1] >= dia + 1):
        print("La fecha es válida")
except:
    print("La fecha no es válida")


def LeerFecha():
    fecha = input("Introduce una fecha (dd/MM/aaaa): ")
    fecha_dividida = fecha.split('/')
    fecha_numerica = [int(fecha_dividida[0]), int(fecha_dividida[1]), int(fecha_dividida[2])]
    return fecha_numerica

def EsBisiesto(año):
    return ((año % 4 == 0 and año % 100 != 0) or (año % 400 == 0))

def DiasDelMes(mes, año):
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if EsBisiesto(año) and mes == 2:
        return 29
    else:
        return dias_por_mes[mes - 1]

def CalcularDiaJuliano(fecha):
    dia_juliano = 0
    for i in range(1, fecha[1]):
        dia_juliano += DiasDelMes(i, fecha[2])

    dia_juliano += fecha[0]
    print(dia_juliano)

fecha = LeerFecha()
CalcularDiaJuliano(fecha)
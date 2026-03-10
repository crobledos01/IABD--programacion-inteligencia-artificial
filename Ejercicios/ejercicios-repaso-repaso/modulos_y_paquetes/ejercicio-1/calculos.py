import areas

# Se generan los resultados de las funciones del módulo areas llamando a las funciones del módulo cadenas
rectangulo = areas.area_rectangulo(5, 9)
triangulo = areas.area_triangulo(5, 13)
circulo = areas.area_circulo(5)

# Se imprimen los resultados
print("Área del rectángulo:", rectangulo)
print("Área del triángulo:", triangulo)
print("Área del círculo:", circulo)
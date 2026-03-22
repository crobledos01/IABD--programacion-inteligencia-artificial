import temperatura

# Se le pide al usuario una temperatura en Celsius
celsius = float(input("Introduce la temperatura en Celsius: "))

# Llamando al módulo, se imprimen los valores convertidos a Fahrenheit y Kelvin
print("Celsius a Fahrenheit:", temperatura.celsius_a_fahrenheit(celsius))
print("Celsius a Kelvin:", temperatura.celsius_a_kelvin(celsius))
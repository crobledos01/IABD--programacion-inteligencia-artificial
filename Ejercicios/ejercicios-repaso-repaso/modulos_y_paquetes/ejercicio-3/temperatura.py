# Esta función convierte una temperatura de Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Esta función convierte una temperatura de Celsius a Kelvin
def celsius_a_kelvin(celsius):
    return celsius + 273.15

# Estas funciones convierten de Fahrenheit y Kelvin a Celsius, respectivamente
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Esta función convierte una temperatura de Kelvin a Celsius
def kelvin_a_celsius(kelvin):
    return kelvin - 273.15
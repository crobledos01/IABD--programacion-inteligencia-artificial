import matplotlib.pyplot as plt
import numpy as np

# Se crea un array para las regiones (eje x) y otro para las incidencias correspondientes (eje Y)
regiones = ["Europa", "América", "Asia", "África", "Oceanía"]
incidencia = np.random.randint(50, 200, size=len(regiones))

# Se crea un gráfico con dimensiones 8x5 en pantalla y se le añaden las regiones y las incidencias
plt.figure(figsize=(8,5))
plt.bar(regiones, incidencia)

# Se añade el título y la información de los ejes al gráfico
plt.title("Tasa de Incidencia de la enfermedad por Región")
plt.xlabel("Región")
plt.ylabel("Casos por 100000 habitantes")
plt.grid(axis="y")

# Se muestra el gráfico anterior
plt.show()

print("\n")

# Se crea un array para los días (eje x) y otro para los casos diarios correspondientes (eje Y)
dias = np.arange(1,31)
casos = np.random.randint(1000, 5000, size=30)

# Calcula muertes como una fracción aleatoria (7%-12%) de los casos diarios
muertes = []
for index, caso in enumerate(casos):
    muertes.append(np.random.randint(int(casos[index] * 0.07), int(casos[index] * 0.12)))

# Se crea un gráfico con dimensiones 10x6 en pantalla y se le añaden los casos y las muertes
plt.figure(figsize=(10,6))
plt.plot(dias, casos, label="Casos", marker="o")
plt.plot(dias, muertes, label="Muertes", marker="x")

# Se añade el título y la información de los ejes al gráfico
plt.title("Evolución de Casos y Muertes en 30 días")
plt.xlabel("Días")
plt.ylabel("Nº personas")
plt.legend()
plt.grid(True)

# Se muestra el gráfico anterior
plt.show()
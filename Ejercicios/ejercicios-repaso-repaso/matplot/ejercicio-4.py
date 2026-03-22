import matplotlib.pyplot as plt
import numpy as np

# Se crea un array para los años (eje x) y otros arrays para el consumo por tipo de energía (eje Y)
años = np.arange(2015,2024)

solar = np.random.randint(10,40,size=len(años))
eolica = np.random.randint(20,50,size=len(años))
fosil = np.random.randint(60,120,size=len(años))

# Se crea un gráfico con dimensiones 10x6 en pantalla y se le añaden los años y el consumo por tipo de energía
plt.figure(figsize=(10,6))

plt.stackplot(años, solar, eolica, fosil,
              labels=["Solar","Eólica","Fósil"],
              colors=["gold","skyblue","gray"])

# Se añade el título y la información de los ejes al gráfico
plt.title("Consumo Energético por Tipo")
plt.xlabel("Año")
plt.ylabel("Consumo energético")
plt.legend()

# Se muestra el gráfico anterior
plt.show()

print("\n")

# Se crea un array para los sectores (eje x) y otro para el consumo correspondiente (eje Y)
sectores = ["Industrial","Residencial","Transporte"]
consumo = [350,220,400]

# Se crea un gráfico con dimensiones 7x5 en pantalla y se le añaden los sectores y el consumo
plt.figure(figsize=(7,5))
plt.bar(sectores, consumo, color=["red","green","blue"])

# Se añade el título y la información de los ejes al gráfico
plt.title("Consumo Energético por Sector")
plt.ylabel("Consumo (GWh)")

# Se muestra el gráfico anterior
plt.show()
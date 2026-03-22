import matplotlib.pyplot as plt
import numpy as np

# Se crea un array para los meses del año (eje x) y otro para los valores de venta correspondientes (eje Y)
meses = ["Ene", "Feb", "Mar", "Abr", "May" ,"Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
ventas = np.random.randint(2000,6000,size=12)

# Se crea un gráfico con dimensiones 8x5 en pantalla y se le añaden los meses y las ventas
plt.figure(figsize=(8,5))
plt.plot(meses, ventas)

# Se añade el título y la información de los ejes al gráfico
plt.title("Evolución de Ventas")
plt.xlabel("Mes")
plt.ylabel("Ventas (€)")
plt.grid(True)

# Se muestra el gráfico anterior
plt.show()

# Separa los gráficos
print("\n")

# Se crea un array para las campañas (eje x) y otro para sus roi correspondientes (eje Y)
campañas = ["Semana Santa","Primavera","Verano","Navidad"]
roi = [150,120,80,200]

# Se crea un gráfico con dimensiones 8x5 en pantalla y se le añaden las camapañs y los roi
plt.figure(figsize=(8,5))
plt.bar(campañas, roi)

# Se añade el título y la información de los ejes al gráfico
plt.title("ROI de Campañas de Marketing")
plt.xlabel("Campaña")
plt.ylabel("ROI (%)")

# Muestra en pantalla el gráfico de barras.
plt.show()
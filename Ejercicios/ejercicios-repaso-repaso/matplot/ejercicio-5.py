import matplotlib.pyplot as plt
import numpy as np

# Se crea un array para los días del mes (eje x) y otro para los valores de venta correspondientes (eje Y)
dias = np.arange(1,31)
visitas = np.random.randint(500,1500,size=30)

# Se crea un gráfico con dimensiones 8x5 en pantalla y se le añaden los meses y las ventas
plt.figure(figsize=(8,5))
plt.plot(dias, visitas)

# Se añade el título y la información de los ejes al gráfico
plt.title("Visitas Web durante el Mes")
plt.xlabel("Día")
plt.ylabel("Número de visitas")
plt.grid(True)

# Se muestra el gráfico anterior
plt.show()

# Separa los gráficos
print("\n")

# Se crea un array para las fuentes de tráfico (eje x) y otro para las visitas correspondientes (eje Y)
fuentes = ["Directo","Redes Sociales","Búsqueda","Referencias"]
visitas_fuente = [3000,2000,4000,1000]

# Dibuja un gráfico de con dimensiones 6x6 en la pantalla y se le añaden meses, visitas, porcentaje de cada una y se ajusta la rotación
plt.figure(figsize=(6,6))
plt.pie(visitas_fuente, labels=fuentes, autopct="%1.1f%%", startangle=90)

# Se añade el título y se muestra el gráfico
plt.title("Fuentes de Tráfico Web")
plt.show()

print("\n")

# Se genera un array aleatorio para el rebote y otro para el tiempo
rebote = np.random.uniform(30,90,50)
tiempo = np.random.uniform(30,300,50)

# Se crea un gráfico con dimensiones 8x5 en pantalla y se le añaden el rebote y el tiempo
plt.figure(figsize=(8,5))
plt.scatter(rebote, tiempo)

# Se añade el título y la información de los ejes al gráfico
plt.title("Relación entre Rebote y Tiempo en Página")
plt.xlabel("Tasa de Rebote (%)")
plt.ylabel("Tiempo en Página (segundos)")

# Muestra en pantalla el gráfico
plt.show()
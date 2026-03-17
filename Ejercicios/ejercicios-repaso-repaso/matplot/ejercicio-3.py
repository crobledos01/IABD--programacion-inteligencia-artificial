import matplotlib.pyplot as plt
import numpy as np

# Se crea un array para los días (eje x) y otro para los posts correspondientes (eje Y)
dias = ["Lun","Mar","Mié","Jue","Vie","Sáb","Dom"]
posts = np.random.randint(20,200,size=7)

# Se crea un gráfico con dimensiones 8x5 en pantalla y se le añaden los días y los posts
plt.figure(figsize=(8,5))
plt.plot(dias, posts, marker="o")

# Se añade el título y la información de los ejes al gráfico
plt.title("Actividad de Publicaciones en Redes Sociales")
plt.xlabel("Día")
plt.ylabel("Nº publicaciones (en miles)")
plt.grid(True)

# Se muestra el gráfico anterior
plt.show()

print("\n")

# Se crea un array para los temas (eje x) y otro para la frecuencia de menciones correspondiente (eje Y)
temas = ["Tecnología","Política","Deportes","Entretenimiento","Educación"]
frecuencia = np.random.randint(300,1000,size=5)

# Se crea un gráfico con dimensiones 8x5 en pantalla y se le añaden los temas y la frecuencia de menciones
plt.figure(figsize=(8,5))
plt.bar(temas, frecuencia)

# Se añade el título y la información de los ejes al gráfico
plt.title("Temas más discutidos en Redes Sociales")
plt.xlabel("Tema")
plt.ylabel("Nº menciones")

# Se muestra el gráfico anterior
plt.show()
# Clase Socio
# Para añadir un socio, debes indicar su nombre, DNI y edad
# Al hacer print de un socio, llama a la función __str__ para mostrar sus datos
class Socio:
    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
    
    def __str__(self):
        return f"Socio: {self.nombre}, DNI: {self.dni}, Edad: {self.edad} años"

# Clase Pelicula
# Para añadir una película, debes indicar su título, género, duración y edad recomendada
# Al hacer print de una película, llama a la función __str__ para mostrar sus datos
class Pelicula:
    def __init__(self, titulo, genero, duracion, edad_recomendada):
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        self.edad_recomendada = edad_recomendada
    
    def __str__(self):
        return f"'{self.titulo}' ({self.genero}, {self.duracion} min) PEGI: {self.edad_recomendada}+"

# Clase Netflix
# Contiene una lista de las clases Pelicula y Socio
class Netflix:
    def __init__(self):
        self.lista_socios = []
        self.lista_peliculas = []
    
    # Se recibe un objeto de la clase Socio y lo añade a la lista
    def alta_socio(self, socio):
        self.lista_socios.append(socio)
        print(f"{socio.nombre} ({socio.dni}) ha sido dado de alta correctamente.")
    
    # Se recibe un DNI, busca el socio en la lista y lo elimina si lo encuentra
    def baja_socio(self, dni):
        for socio in self.lista_socios:
            if socio.dni == dni:
                self.lista_socios.remove(socio)
                print(f"{socio.nombre} ({socio.dni}) ha sido dado de baja correctamente.")
                return
        print(f"No se ha encontrado el socio con el DNI {dni}.")
    
    # Esta función muestra todos los socios de la lista. Si no hay socios, se indica
    def mostrar_socios(self):
        if not self.lista_socios:
            print("No hay socios registrados.")
        else:
            print("\n\nLista de socios:\n")
            for socio in self.lista_socios:
                print(socio)
    
    # Se recibe un objeto de la clase Pelicula y la añade a la lista
    def alta_pelicula(self, pelicula):
        self.lista_peliculas.append(pelicula)
        print(f"'{pelicula.titulo}' se ha añadida al catálogo.")
    
    # Se recibe un título, busca la película en la lista y la elimina si la encuentra
    def baja_pelicula(self, titulo):
        for pelicula in self.lista_peliculas:
            if pelicula.titulo.lower() == titulo.lower():
                self.lista_peliculas.remove(pelicula)
                print(f"'{titulo}' ha sido eliminada del catálogo.")
                return
        print(f"No seha encontrado la película '{titulo}'.")
    
    # Esta función muestra todas las películas de la lista. Si no hay películas, se indica
    def mostrar_peliculas(self):
        if not self.lista_peliculas:
            print("No hay películas registradas.")
        else:
            print("\n\nLista de películas:\n")
            for pelicula in self.lista_peliculas:
                print(pelicula)
    
    # Muestra la cantidad de socios y películas registradas al llamar a la clase Netflix
    def __str__(self):
        return f"Netflix tiene {len(self.lista_socios)} socios y {len(self.lista_peliculas)} películas."

netflix = Netflix()

abandonar = False
while not abandonar:
    print("\n--- Menú de opciones ---")
    print("1. Dar de alta un socio")
    print("2. Dar de baja un socio")
    print("3. Mostrar socios")
    print("4. Dar de alta una película")
    print("5. Dar de baja una película")
    print("6. Mostrar películas")
    print("7. Muestra la cantidad de socios y películas")
    print("0. Salir")
    
    opcion = input("\nSelecciona una opción: ")
    
    match opcion:
        case '1':
            nombre = input("Indica el nombre:")
            dni = input("Indica el DNI:")
            edad = int(input("Indica la edad:"))
            nuevo_socio = Socio(nombre, dni, edad)
            netflix.alta_socio(nuevo_socio)
        
        case '2':
            dni = input("Indica el DNI del socio a dar de baja:")
            netflix.baja_socio(dni)
        
        case '3':
            netflix.mostrar_socios()
        
        case '4':
            titulo = input("Indica el título de la película:")
            genero = input("Indica el género de la película:")
            duracion = int(input("Indica la duración de la película (en minutos):"))
            edad_recomendada = int(input("Indica la edad recomendada para la película:"))
            nueva_pelicula = Pelicula(titulo, genero, duracion, edad_recomendada)
            netflix.alta_pelicula(nueva_pelicula)
        
        case '5':
            titulo = input("Título de la película a dar de baja:")
            netflix.baja_pelicula(titulo)
        
        case '6':
            netflix.mostrar_peliculas()
        
        case '7':
            print(netflix)

        case '0':
            abandonar = True
            
        case _:
            print("Opción no válida, por favor selecciona una opción del 0 al 7.")
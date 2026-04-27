from abc import ABC, abstractmethod

# Clase Producto
# Se crea la interfaz común para los 3 tipos de productos y se añaden los métodos abstractos de cálculo de precio e información del producto
class Producto(ABC):
    def __init__(self, nombre, precio, descripcion, esta_oferta=False):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.esta_oferta = esta_oferta

    @abstractmethod
    def calcular_precio(self):
        pass

    @abstractmethod
    def mostrar_informacion(self):
        pass

# Clase Libro
# Implementa la interfaz para libros, necesita autor para mostrar la información del producto
# Se añaden los métodos de cálculo de precio con un descuento si el producto está en oferta y de muestra de la información
class Libro(Producto):
    def __init__(self, nombre, precio, descripcion, autor, esta_oferta=False):
        super().__init__(nombre, precio, descripcion, esta_oferta)
        self.autor = autor

    def calcular_precio(self):
        if self.esta_oferta:
            return self.precio * 0.8
        return self.precio

    def mostrar_informacion(self):
        print(f"Libro: {self.nombre}")
        print(f"Autor: {self.autor}")
        print(f"Descripción: {self.descripcion}")
        if self.esta_oferta:
            print(f"Precio: {self.precio * 0.8}€ (oferta)")
        else:
            print(f"Precio: {self.precio}€")


# Clase Disco
# Implementa la interfaz para discos, necesita artista para mostrar la información del producto
# Se añaden los métodos de cálculo de precio con un descuento si el producto está en oferta y de muestra de la información
class Disco(Producto):
    def __init__(self, nombre, precio, descripcion, artista, esta_oferta=False):
        super().__init__(nombre, precio, descripcion, esta_oferta)
        self.artista = artista

    def calcular_precio(self):
        if self.esta_oferta:
            return self.precio * 0.7
        return self.precio

    def mostrar_informacion(self):
        print(f"Disco: {self.nombre}")
        print(f"Artista: {self.artista}")
        print(f"Descripción: {self.descripcion}")
        if self.esta_oferta:
            print(f"Precio: {round(self.precio * 0.7, 2):.2f}€ (oferta)")
        else:
            print(f"Precio: {self.precio}€")


# Clase Electrónico
# Implementa la interfaz para electrónicos, necesita marca para mostrar la información del producto
# Se añaden los métodos de cálculo de precio con un descuento si el producto está en oferta y de muestra de la información
class Electronico(Producto):
    def __init__(self, nombre, precio, descripcion, marca, esta_oferta=False):
        super().__init__(nombre, precio, descripcion, esta_oferta)
        self.marca = marca

    def calcular_precio(self):
        if self.esta_oferta:
            return round(self.precio * 0.9, 2)
        return round(self.precio, 2)

    def mostrar_informacion(self):
        print(f"Electrónico: {self.nombre}")
        print(f"Marca: {self.marca}")
        print(f"Descripción: {self.descripcion}")
        print(f"Precio original: {self.precio} €")
        if self.esta_oferta:
            print(f"Precio: {round(self.precio * 0.9, 2):.2f}€ (oferta)")
        else:
            print(f"Precio: {self.precio}€")
        print("\n-----------------------------\n")

# Clase Tienda
# Se crea la clase tienda que contiene una lista de productos
# Se añaden métodos para agregar, mostrar productos y buscar productos, y calcular el precio total de todos los productos
class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        if not self.productos:
            print("\nNo hay productos en la tienda.")
            return

        print("\nPRODUCTOS DE LA TIENDA:")
        for producto in self.productos:
            producto.mostrar_informacion()

    # Esta función recorre la lista de productos y devuelve las coincidencias con el nombre o la descripción en mayúculas
    def buscar_productos(self, texto):
        resultados = []
        texto = texto.lower()

        for producto in self.productos:
            if texto in producto.nombre.lower() or texto in producto.descripcion.lower():
                resultados.append(producto)

        return resultados

    def calcular_precio_total(self):
        total = sum(producto.calcular_precio() for producto in self.productos)
        print(f"\nPrecio total de todos los productos: {total}€")
        return total

tienda = Tienda()

# Se crea un menú para que el usuario pueda interactuar con la tienda usando los números del 0 al 4
while True:
    print("\nMENÚ DE LA TIENDA")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar productos")
    print("4. Calcular precio total")
    print("0. Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        # Se agrega un producto a la tienda. Se pide al usuario el tipo de producto y los datos generales
        case "1":
            print("\nTIPO DE PRODUCTO")
            print("1. Libro")
            print("2. Disco")
            print("3. Electrónico")

            tipo = input("Elige el tipo de producto: ")

            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            descripcion = input("Descripción: ")
            esta_oferta = input("¿Está de oferta? (s/n): ").lower() == "s"

            # Se realiza otro match para crear el producto específico según el tipo elegido y se añade a la tienda
            match tipo:
                case "1":
                    autor = input("Autor: ")
                    producto = Libro(nombre, precio, descripcion, autor, esta_oferta)

                case "2":
                    artista = input("Artista: ")
                    producto = Disco(nombre, precio, descripcion, artista, esta_oferta)

                case "3":
                    marca = input("Marca: ")
                    producto = Electronico(nombre, precio, descripcion, marca, esta_oferta)

                case _:
                    print("\nTipo de producto no válido.")
                    pass
            
            tienda.agregar_producto(producto)
            print("Producto electrónico agregado correctamente.")

        # LLama a la función mostrar_prductos para mostrar todos los productos de la tienda
        case "2":
            tienda.mostrar_productos()

        # Se pide al usuario un texto para buscar productos por nombre o descripción
        # Se muestran los resultados llamando a la función mostrar_informacion (pueden ser varios)
        case "3":
            texto = input("Introduce el texto a buscar: ")
            resultados = tienda.buscar_productos(texto)

            if resultados:
                print("\nRESULTADOS DE LA BÚSQUEDA:")
                for producto in resultados:
                    producto.mostrar_informacion()
            else:
                print("\nNo se encontraron productos.")

        # Se llama a la función que calcula el precio de todos los productos
        case "4":
            tienda.calcular_precio_total()

        # Sale del programa
        case "0":
            print("Saliendo del programa.")
            break

        case _:
            print("\nOpción no válida.")
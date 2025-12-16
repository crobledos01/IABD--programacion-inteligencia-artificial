#Saca la longitud del array biblioteca para obtener la cantidad. Se utiliza en el punto 3 y en el 5.
def total_libros():
    cantidad = len(biblioteca)
    return cantidad

#Pide al usuario la cantidad de libros que quiere añadir y crea un bucle desde 0 hasta ese número.
#Después, pide al usuario los datos de cada libro y los añade al array. En leido o no, se pide 0 o 1 ya que se pueden convertir en bool y
#                                                                                       meterlos directamente al objeto como True o False
def agregar_libros():
    cantidad = int(input("¿Cuántos libros quieres añadir? "))
    for i in range(0, cantidad):
        print(f"Libro número {i + 1}")
        titulo = input("Añade el título del libro: ")
        autor = input("Añade el autor del libro: ")
        fecha = int(input("Añade el año de publicación del libro: "))
        leido = bool(int(input("Añade un 1 si el libro está leído y un 0 si no: ")))
        print()
        libro = {
            "titulo": titulo,
            "autor": autor,
            "fecha": fecha,
            "leido": leido
        }
        biblioteca.append(libro)

#Primero se crea una variable para los libros leídos y otra para los no leídos.
#Después, se recorre el array biblioteca y se comprueba que el valor "leido" sea True. En caso positivo se añade a leidos y en el negativo a no leidos
#Por último, se imprime en pantalla la cantidad de cada uno
def contar_libros():
    leidos = 0
    no_leidos = 0
    for libro in biblioteca:
        if(libro["leido"]):
            leidos = leidos + 1
        else:
            no_leidos = no_leidos + 1

    print("Tienes", leidos, "libros leídos y", no_leidos, "sin leer")

#Primero se recoge la cantidad de libros. Si es cero, simplemente se indica al usuario que no hay libros disponibles
#En caso de que si haya libros, se crea una variable con la suma de todas las flechas con valor a 0 y recorre el array para ir sumando cada una
#Por último, se realiza una media, se pasa a int para que de un número entero y se imprime por consola
def media_fecha_publicacion():
    cantidad = total_libros()
    if(cantidad == 0):
        print("No hay libros disponibles, así que no se puede calcular una fecha media.")
    else:
        total_fechas = 0
        for libro in biblioteca:
            total_fechas = total_fechas + libro["fecha"]

        media = int(total_fechas / cantidad)
        print("El año medio de publicación de los libros es:", media)

#Primero se pide el nombre del autor. Después, se crea una variable para saber si se ha encontrado resultados o no.
#Se hace un bucle para recorrer todos los valores de biblioteca, utilizando un if para ver si coincide el autor del libro con el introducido
#La primera vez que encuentra uno, evita poner la coma, setea a True la variable de que existe el autor
#Cada vez que encuentra un resultado, imprime el título del libro junto a la fecha entre paréntesis
#Por último, comprueba si existe o no el autor en la biblioteca y lo indica en caso de que no exista
def libros_autor():
    autor = input("Introduce el nombre del autor: ")
    print()
    autor_existe = False
    for libro in biblioteca:
        if libro["autor"] == autor:
            if autor_existe:
                print(end=", ")
            autor_existe = True
            print(f"{libro["titulo"]} ({libro["fecha"]})", end="")

    if autor_existe == False:
        print("No se han encontrado libros del autor", end="")
    
    print()

#Llama a las diversas funciones creadas anteriormente para mostrar un resumen de la info
def mostrar_conjunto():
    libros = total_libros()
    print("El total de libros es:", libros)
    contar_libros()
    media_fecha_publicacion()

#Se hace un bucle que imprime todo el contenido del bucle indicando Titulo, Autor (fecha). Leido/No
def lista_libros():
    for libro in biblioteca:
        print(f"{libro["titulo"]}, {libro["autor"]} ({libro["fecha"]}).", end=" ")
        if libro["leido"]:
            print("Leído")
        else:
            print("No leído")
        

#Se crea el array de biblioteca y una variable exit para que el usuario salga de la aplicación cuando no quiera hacer más operaciones.
#Después se crea un bucle con while que continuará hasta que el usuario lo indique seteando el valor de exit a True
#Se indica al usuario el numero que sirve para realizar cada acción y se le pide que introduzca uno
#Por ultimo, match analiza el número que el usuario ha introducido y llama a la función correspondiente en base a este, o setea exit a true si elige el 0
biblioteca = []
exit = False
while exit != True:
    print()
    print("0. Cerrar aplicación.")
    print("1. Añadir libros a la biblioteca.")
    print("2. Contar los libros leídos y no leídos.")
    print("3. Mostrar la fecha de publicación media de los libros.")
    print("4. Mostrar todos los libros de un autor.")
    print("5. Mostrar total de libros, cantidad de leídos y no leídos, y año medio de publicación.")
    print("6. Lista completa de todos los libros.")
    accion = int(input("Introduce un número para realizar la acción indicada: "))
    print()
    
    match accion:
        case 0:
            exit = True
        case 1:
            agregar_libros()
        case 2:
            contar_libros()
        case 3:
            media_fecha_publicacion()
        case 4:
            libros_autor()
        case 5:
            mostrar_conjunto()
        case 6:
            lista_libros()
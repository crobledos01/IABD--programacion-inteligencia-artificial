usuario = "pepe"
contrasena = "asdasd"
input_usuario = input("Introduce tu usuario: ")
input_contrasena = input("Introduce tu contraseña: ")
if input_usuario == usuario and input_contrasena == contrasena:
    print("Has entrado al sistema")
else:
    print("Usuario o contraseña incorrectos, pero no te voy a decir cuál de los dos")
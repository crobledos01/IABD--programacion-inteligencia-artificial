# Comprueba si una expresión tiene paréntesis, corchetes y llaves equilibrados
def expresion_equilibrada(expresion):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}
    # Recorre cada carácter de la expresión
    for caracter in expresion:
        # Si es un símbolo de apertura, lo añade a la pila
        if caracter in "({[":
            pila.append(caracter)
        elif caracter in ")}]":
            # Si la pila está vacía o el último abierto no coincide, no está equilibrada
            if not pila or pila[-1] != pares[caracter]:
                return False
            pila.pop()
    # Si la pila está vacía, está equilibrada
    return len(pila) == 0

# Solicita una expresión al usuario y muestra si está equilibrada
exp = input("Introduce una expresión: ")
if expresion_equilibrada(exp):
    print(f"La expresión {exp} está equilibrada")
else:
    print(f"La expresión {exp} NO está equilibrada")
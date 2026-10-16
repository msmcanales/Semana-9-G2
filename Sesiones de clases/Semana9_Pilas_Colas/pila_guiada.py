pila = []

def apilar(libro):
    pila.append(libro)
    print(f"Libro agregado: {libro}")

def desapilar():
    if len(pila) == 0:
        print("La pila está vacía")
    else:
        libro = pila.pop()
        print(f"Libro retirado: {libro}")

def mostrar_pila():
    if not pila:
        print("No hay libros")
    else:
        print("Pila actual:", pila)
        print("Libro en el tope:", pila[-1])

while True:
    print("\n--- MENÚ DE PILA DE LIBROS ---")
    print("1. Agregar libro")
    print("2. Retirar libro")
    print("3. Mostrar pila")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        libro = input("Ingrese el nombre del libro: ")
        apilar(libro)

    elif opcion == "2":
        desapilar()

    elif opcion == "3":
        mostrar_pila()

    elif opcion == "4":
        print("Programa finalizado")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
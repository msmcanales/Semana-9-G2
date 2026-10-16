
# reto1_bodega.py
# Sistema de cajas usando una pila LIFO

pila = []


def apilar():
    codigo = input("Ingrese el código de la caja: ").strip().upper()

    # Validar que el código no esté vacío ni repetido
    if not codigo:
        print("Error: el código no puede estar vacío.")
    elif codigo in pila:
        print("Error: ese código ya existe.")
    else:
        pila.append(codigo)
        print(f"Caja {codigo} agregada correctamente.")
        print(f"Cantidad de cajas: {len(pila)}")


def desapilar():
    # Evitar retirar cajas de una pila vacía
    if not pila:
        print("La bodega está vacía. No se puede retirar.")
    else:
        codigo = pila.pop()
        print(f"Caja retirada: {codigo}")
        print(f"Cantidad de cajas: {len(pila)}")


def consultar_tope():
    if not pila:
        print("La bodega está vacía.")
    else:
        print(f"Caja en el tope: {pila[-1]}")


def mostrar_pila():
    if not pila:
        print("La bodega está vacía.")
        print("Cantidad de cajas: 0")
        return

    # Dibujar las cajas desde el tope hasta la base
    ancho = max(22, max(len(c) + 10 for c in pila))
    borde = "+" + "-" * ancho + "+"

    print("\n       PILA DE CAJAS")
    print("          (TOPE)")
    print(borde)

    for codigo in reversed(pila):
        contenido = f"  CAJA: {codigo}"
        print("|" + contenido.ljust(ancho) + "|")
        print(borde)

    print("          (BASE)")
    print(f"Cantidad de cajas: {len(pila)}")


def menu():
    while True:
        print("\n===== SISTEMA DE BODEGA =====")
        print("1. Apilar caja")
        print("2. Desapilar caja")
        print("3. Consultar tope")
        print("4. Mostrar pila")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            apilar()
        elif opcion == "2":
            desapilar()
        elif opcion == "3":
            consultar_tope()
        elif opcion == "4":
            mostrar_pila()
        elif opcion == "5":
            print("Sistema de bodega finalizado.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# Iniciar el programa
if __name__ == "__main__":
    menu()

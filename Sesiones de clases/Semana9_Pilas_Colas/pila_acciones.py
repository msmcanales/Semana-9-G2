
acciones = []

def registrar_accion(descripcion):
    acciones.append(descripcion)
    print("Acción registrada:", descripcion)


def deshacer():
    if not acciones:
        print("No existen acciones para deshacer.")
        return

    ultima = acciones.pop()
    print("Se deshizo:", ultima)


def historial():
    if not acciones:
        print("El historial está vacío.")
    else:
        print("\nAcciones pendientes:")
        for i, accion in enumerate(acciones, start=1):
            print(f"{i}. {accion}")


def mostrar_menu():
    print("\n===== MENÚ DE ACCIONES =====")
    print("1. Registrar acción")
    print("2. Deshacer última acción")
    print("3. Mostrar historial")
    print("4. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            descripcion = input(
                "Ingrese la descripción de la acción: "
            ).strip()

            if descripcion:
                registrar_accion(descripcion)
            else:
                print("Error: la descripción no puede estar vacía.")

        elif opcion == "2":
            deshacer()

        elif opcion == "3":
            historial()

        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Error: opción inválida. Ingrese un número del 1 al 4.")


if __name__ == "__main__":
    main()

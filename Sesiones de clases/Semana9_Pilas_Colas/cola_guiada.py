
from collections import deque

# Cola de pacientes
cola = deque()


def registrar_paciente(nombre):
    nombre = nombre.strip()

    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    cola.append(nombre)
    print(f"Registrado: {nombre}")


def atender_paciente():
    if not cola:
        print("No hay pacientes en espera.")
    else:
        paciente = cola.popleft()
        print(f"Atendiendo a: {paciente}")


def mostrar_cola():
    if not cola:
        print("La cola está vacía.")
    else:
        print("Pacientes en espera:")
        for posicion, paciente in enumerate(cola, 1):
            print(f"{posicion}. {paciente}")


def menu():
    while True:
        print("\n===== SISTEMA DE ATENCIÓN DE PACIENTES =====")
        print("1. Registrar paciente")
        print("2. Atender paciente")
        print("3. Mostrar cola")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Ingrese el nombre del paciente: ")
            registrar_paciente(nombre)

        elif opcion == "2":
            atender_paciente()

        elif opcion == "3":
            mostrar_cola()

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    # Ejemplo inicial
    registrar_paciente("Ana")
    registrar_paciente("Luis")
    registrar_paciente("María")
    mostrar_cola()
    atender_paciente()
    mostrar_cola()

    # Menú interactivo
    menu()

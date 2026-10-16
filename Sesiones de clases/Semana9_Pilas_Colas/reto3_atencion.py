
from collections import deque


class SistemaAtencion:
    def __init__(self):
        self.cola = deque()
        self.siguiente_turno = 1

    def registrar_cliente(self, nombre):
        nombre = nombre.strip()

        if not nombre:
            print("Error: el nombre no puede estar vacío.")
            return False

        cliente = {
            "turno": self.siguiente_turno,
            "nombre": nombre
        }

        self.cola.append(cliente)
        print(
            f"Turno {cliente['turno']} registrado "
            f"para {cliente['nombre']}."
        )
        self.siguiente_turno += 1
        return True

    def atender_cliente(self):
        if not self.cola:
            print("No hay clientes pendientes.")
            return

        cliente = self.cola.popleft()
        print(
            f"Atendiendo turno {cliente['turno']}: "
            f"{cliente['nombre']}."
        )

    def consultar_proximo(self):
        if not self.cola:
            print("No hay clientes en espera.")
            return

        cliente = self.cola[0]
        print(
            f"Próximo cliente: turno {cliente['turno']} - "
            f"{cliente['nombre']}."
        )

    def mostrar_cola(self):
        if not self.cola:
            print("La cola está vacía.")
            return

        print("\n--- Clientes en espera ---")
        for cliente in self.cola:
            print(
                f"Turno {cliente['turno']}: "
                f"{cliente['nombre']}"
            )

    def cantidad_pendientes(self):
        cantidad = len(self.cola)
        print(f"Clientes pendientes: {cantidad}")
        return cantidad


def mostrar_menu():
    print("\n===== SISTEMA DE ATENCIÓN =====")
    print("1. Registrar cliente")
    print("2. Atender siguiente cliente")
    print("3. Consultar próximo cliente")
    print("4. Mostrar clientes en espera")
    print("5. Mostrar cantidad de pendientes")
    print("6. Salir")
    return input("Seleccione una opción: ").strip()


def main():
    sistema = SistemaAtencion()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            sistema.registrar_cliente(nombre)

        elif opcion == "2":
            sistema.atender_cliente()

        elif opcion == "3":
            sistema.consultar_proximo()

        elif opcion == "4":
            sistema.mostrar_cola()

        elif opcion == "5":
            sistema.cantidad_pendientes()

        elif opcion == "6":
            print("Sistema finalizado. ¡Hasta pronto!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()

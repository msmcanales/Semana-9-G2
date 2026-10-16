
historial = []
pagina_actual = None


def registrar_pagina(url):
    global pagina_actual

    url = url.strip()

    if not url:
        print("Error: la dirección no puede estar vacía.")
        return

    if pagina_actual is not None:
        historial.append(pagina_actual)

    pagina_actual = url
    print("Visitando:", pagina_actual)


def regresar():
    global pagina_actual

    if not historial:
        print("No existen páginas anteriores")
        return

    pagina_actual = historial.pop()
    print(pagina_actual)


def consultar_pagina():
    if pagina_actual is None:
        print("No hay ninguna página abierta.")
    else:
        print("Página actual:", pagina_actual)


def mostrar_historial():
    if not historial:
        print("No hay páginas anteriores.")
    else:
        print("Historial pendiente de retroceso:")
        for pagina in reversed(historial):
            print(pagina)


def menu():
    while True:
        print("\n--- SIMULADOR DE NAVEGADOR ---")
        print("1. Registrar página web")
        print("2. Regresar")
        print("3. Consultar página actual")
        print("4. Mostrar historial")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            url = input("Ingrese la URL: ")
            registrar_pagina(url)
        elif opcion == "2":
            regresar()
        elif opcion == "3":
            consultar_pagina()
        elif opcion == "4":
            mostrar_historial()
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()

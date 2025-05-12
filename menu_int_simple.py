def saludar():
    """Imprime un saludo."""
    print("¡Hola! ¡Bienvenido!")

def decir_edad():
    """Imprime una respuesta sobre la edad."""
    print("Como soy una inteligencia artificial, no tengo edad en la forma en que los humanos la entienden.")

def mostrar_menu():
    """Muestra las opciones del menú."""
    print("\n--- Menú ---")
    print("1. Saludar")
    print("2. Decir tu edad")
    print("3. Salir")
    print("------------")

def main():
    """Función principal para el menú interactivo."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == '1':
            saludar()
        elif opcion == '2':
            decir_edad()
        elif opcion == '3':
            print("¡Hasta luego!")
            break  # Sale del bucle while
        else:
            print("Opción inválida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()
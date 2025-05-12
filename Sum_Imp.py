def sumar_impares_hasta():
    """Pide un número al usuario y suma todos los números impares desde 1 hasta ese número (inclusive) usando un ciclo for."""
    while True:
        try:
            numero_limite = int(input("Ingrese un número entero positivo: "))
            if numero_limite > 0:
                break
            else:
                print("Por favor, ingrese un número entero positivo.")
        except ValueError:
            print("¡Error! Por favor, ingrese un número entero válido.")

    suma_impares = 0
    for i in range(1, numero_limite + 1, 2):
        suma_impares += i

    print(f"La suma de los números impares entre 1 y {numero_limite} es: {suma_impares}")

if __name__ == "__main__":
    sumar_impares_hasta()
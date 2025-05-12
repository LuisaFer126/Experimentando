def tabla_de_multiplicar():
    """Pide un número al usuario y muestra su tabla de multiplicar del 1 al 10 usando un bucle while."""
    while True:
        try:
            numero = int(input("Ingrese un número entero para ver su tabla de multiplicar: "))
            break
        except ValueError:
            print("¡Error! Por favor, ingrese un número entero válido.")

    print(f"\nTabla de multiplicar del {numero}:")
    i = 1
    while i <= 10:
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
        i += 1

if __name__ == "__main__":
    tabla_de_multiplicar()
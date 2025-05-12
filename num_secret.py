def adivina_el_secreto():
    """Pide al usuario que adivine un número secreto hasta que lo acierte."""
    numero_secreto = 7
    intentos = 0

    print("¡Adivina el número secreto!")
    print("Está entre 1 y 10.")  # Damos una pista del rango

    while True:
        intentos += 1
        while True:
            try:
                intento = int(input("Ingresa tu intento: "))
                if 1 <= intento <= 10:
                    break
                else:
                    print("Por favor, ingresa un número entre 1 y 10.")
            except ValueError:
                print("¡Error! Por favor, ingresa un número entero válido.")

        if intento == numero_secreto:
            print(f"¡Felicidades! ¡Adivinaste el número secreto ({numero_secreto}) en {intentos} intentos!")
            break
        else:
            print("¡Intento incorrecto! Sigue probando.")

if __name__ == "__main__":
    adivina_el_secreto()
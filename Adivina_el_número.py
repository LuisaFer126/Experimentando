import random

def adivinar_numero_inteligente():
    """Juego de adivinar el número con pistas inteligentes."""
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        intentos += 1
        while True:
            try:
                intento = int(input("Intenta adivinar el número: "))
                if 1 <= intento <= 100:
                    break
                else:
                    print("Por favor, ingresa un número entre 1 y 100.")
            except ValueError:
                print("¡Error! Por favor, ingresa un número entero válido.")

        if intento == numero_secreto:
            print(f"¡Felicidades! ¡Adivinaste el número {numero_secreto} en {intentos} intentos!")
            break
        else:
            diferencia = abs(intento - numero_secreto)
            if intento < numero_secreto:
                print("El número secreto es mayor.")
            else:
                print("El número secreto es menor.")

            if diferencia >= 20:
                print("Estás muy lejos.")
            elif 10 <= diferencia < 20:
                print("Estás cerca.")
            else:  # 1 <= diferencia < 10
                print("Estás muy cerca.")

if __name__ == "__main__":
    adivinar_numero_inteligente()
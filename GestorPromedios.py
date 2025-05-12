def solicitar_datos_estudiante():
    """Solicita el nombre y las tres notas de un estudiante."""
    nombre = input("Ingrese el nombre del estudiante: ")
    notas = []
    for i in range(3):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i+1} (de 0 a 5) para {nombre}: "))
                if 0 <= nota <= 5:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 5.")
            except ValueError:
                print("¡Error! Por favor, ingrese un número válido para la nota.")
    return nombre, notas

def calcular_promedio(notas):
    """Calcula el promedio de una lista de notas."""
    if not notas:
        return 0
    return sum(notas) / len(notas)

def mostrar_resultado(nombre, promedio):
    """Muestra el nombre del estudiante y si aprueba o reprueba según su promedio."""
    print(f"\n--- Resultados de {nombre} ---")
    print(f"Promedio: {promedio:.2f}")
    if promedio >= 3.0:
        print(f"{nombre} ha aprobado.")
    else:
        print(f"{nombre} ha reprobado.")

def main():
    """Función principal para gestionar el cálculo de promedios de estudiantes."""
    while True:
        try:
            num_estudiantes = int(input("Ingrese la cantidad de estudiantes a evaluar: "))
            if num_estudiantes > 0:
                break
            else:
                print("Por favor, ingrese un número positivo de estudiantes.")
        except ValueError:
            print("¡Error! Por favor, ingrese un número entero válido.")

    for _ in range(num_estudiantes):
        nombre, notas = solicitar_datos_estudiante()
        promedio = calcular_promedio(notas)
        mostrar_resultado(nombre, promedio)

if __name__ == "__main__":
    main()
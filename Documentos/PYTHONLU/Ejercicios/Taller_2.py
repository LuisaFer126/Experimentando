# Gestión de Calificaciones y Estadísticas


def approval_status():
 while True:
    try:
         Entry = (input("Ingrese una calificación: "))
         if Entry. lower() == "salir":
            break
         Score= float(Entry)
         if Score >= 0 and Score<= 59:
            print("Usted Reprobó")
         elif Score > 59 and Score < 70 : 
            print("Usted Aprovó con un puntaje bajo")
         elif Score >= 70 and Score < 80 :
            print("Usted Aprovó satistactoriamente ")
         elif Score >= 80 and Score < 90 :
            print("¡Felicidades! usted Aprovó con un buen puntaje")
         elif Score >=90 and Score < 100 :
            print("¡Felicidades! usted aprovó sobresalientemente")
         elif Score == 100 :
            print("¡Excelente trabajo! Su calificación fue perfecta")
         elif Score < 0:
            print("Error: Por favor ingresa un número positivo para la calificación")
         elif Score > 100:
            print("Error: La calificación máxima es 100")
    except ValueError:
       print("Error: Por favor ingresa un número válido.")
       
print("------------------------------------------------------------------------------------------")

def average_calculator():
 while True:
   try:
    print("Ahora calculemos tu promedio")
    Grades = list(map(float, input("ingrese sus calificaciones separadas por comas: ").split(',')))
    average = sum(Grades)/len(Grades) 
    print(f"Su promedio es:  "{average:.2f})
    break
   except ValueError:
     print("Ingrese una lista de calificaciones numéricas válidas.")


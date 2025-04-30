# Gestión de Calificaciones y Estadísticas


def approval_status():
   print("Veamos si Aprobaste o Reprobaste")
   while True:
    try:
         Score = float(input("Ingrese una calificación: "))
      
         if Score >= 0 and Score<= 59:
            print("Usted Reprobó")
         elif Score > 59 and Score < 70 : 
            print("Usted Aprobó con un puntaje bajo")
         elif Score >= 70 and Score < 80 :
            print("Usted Aprobó satistactoriamente ")
         elif Score >= 80 and Score < 90 :
            print("¡Felicidades! usted Aprobó con un buen puntaje")
         elif Score >=90 and Score < 100 :
            print("¡Felicidades! usted aprobó sobresalientemente")
         elif Score == 100 :
            print("¡Excelente trabajo! Su calificación fue perfecta")
         elif Score < 0:
            print("Error: Por favor ingresa un número positivo para la calificación")
         elif Score > 100:
            print("Error: La calificación máxima es 100")
    except ValueError:
       print("Error: Por favor ingresa un número válido.")

def average_calculator():
 while True:
   try:
     print("Ahora calculemos tu promedio")
     Grades = list(map(float, input("ingrese sus calificaciones separadas por comas: ").split(',')))
     average = sum(Grades)/len(Grades)
     print(f"Su promedio es:  {average:.2f}")
     break
   except ValueError:
     print("Ingrese una lista de calificaciones numéricas válidas.")

def major_rating():
   while True:
      try:
         Grades = list(map(float,input("Ingrese una lista de calificacines separadas por comas:  ").split(',')))
         Specific_value = float(input("Ingrese un valor específico para comparar:  "))
         count = sum(1 for score in Grades if score > Specific_value)
         print(f"Hay {count}calificaciones mayores que {Specific_value}")
         break
      except ValueError:
         print("Ingrese valores numéricos válidos.")

def verify_specific_score():
   while True:
      try:
         Grades = list(map(float, input))



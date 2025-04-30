#Clasificación de usuarios por edades

while True:
    entrada= input("Digita tu edad(o escribe 'salir' para terminar): ")
    if entrada.lower() == "salir":
         break
    try:
     Edad = int(entrada)
     if Edad<0:
      print("Error: Por favor, ingresa un número positivo para la edad")
     elif Edad < 12 and Edad>0:
       print ("Eres un niño")
     elif Edad>=12 and Edad <=17:
       print ("Eres un adolescente")
     elif Edad >=18 and Edad <=59:
       print ("Eres un adulto")
     elif Edad >= 60:
      print ("Eres un adulto mayor")
    except ValueError:
     print("Error: Por favor ingresa un número entero válido o 'salir'.")


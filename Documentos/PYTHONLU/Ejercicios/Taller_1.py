#Mensajes de bienvenida.
print("¡Bienvenido a nuestra Tienda!")
print("...Calculemos el costo total de tu compra...")

#Función que define las variables correctas para indicar el precio del producto y sus debidos condicionales.
def obtener_precio(): 
 while True:
     try: 
        precio= float(input("Ingrese el precio unitario del producto:  "))
        if precio > 0:
           return precio
        else:
           print("El precio debe ser un número positivo.")
     except ValueError:
        print("Ingrese un número válido.")

#Función que define las variables correctas que pueden ser ingresadas en el enunciado de la cantidad del producto junto con los condicionales requeridos.
def obtener_cantidad():
   while True:
      try:
         cantidad= int(input("Ingrese la cantidad de productos que desea llevar:  "))
         if cantidad > 0:
            return cantidad
         else:
            print("La cantidad debe ser un número entero positivo.")
      except ValueError:
         print("ingrese un número entero válido.")

#Función y condicionales que determina las variables correctas que pueden ser ingresadas en el indicador de descuento.
def obtener_descuento():
   while True:
      try:
         descuento= float(input("Ingrese el porcentaje de descuento(0-100)"))
         if 0 <= descuento <= 100:
            return descuento
         else:
            print("El descuento debe ser entre 0 y 100.")
      except ValueError:
           print("Ingrese un número válido.")

#Función con las operaciones matemáticas necesarias para cada indicador.
def Calcular_costo_total(precio, cantidad, descuento):
   costo_sin_descuento= precio*cantidad
   descuento_monto= costo_sin_descuento*(descuento/100)
   costo_total= costo_sin_descuento-descuento_monto
   return costo_total

# Función del resultado final.
def main():
   nombre_producto= input("Ingrese el nombre del producto:  ")
   precio= obtener_precio()
   cantidad= obtener_cantidad()
   descuento= obtener_descuento()
   costo_total= Calcular_costo_total(precio, cantidad,descuento)
   print("--------------------------------------------------------------------------------------------------")
   print(f"Producto: {nombre_producto}")
   print(f"Costo Total: $ {costo_total:.2f}")

if __name__ == "__main__": main()
   
# DIGITAL INVENTARY

#This Function defines the firt option in the menu. Here the user can add as many products as he wants in the inventary.
def Product_in(inventario):
    try:
        amount = int(input("Ingrese la Cantidad de productos a inventariar: "))
        if amount <= 0:
            print("La cantidad debe ser un número positivo")
            return inventario  # Return the inventary without changes
    except ValueError:
        print("¡Error! Por favor, ingrese un número entero válido para la cantidad.")
        return inventario  # Return the inventary without changes

# This is a loop. With this the user can add the quantity of product he wants.
    for i in range(amount):
        print(f"\nIngrese los datos del producto #{i+1}: ")
        product_name = input("Ingrese el nombre del producto: ").strip()
        while True:
            try:
                product_value = float(input("Ingrese el precio del producto: "))
                amount_product = int(input("Ingrese la cantidad de producto disponible: "))
                if product_value <= 0 or amount_product < 0:
                    print("¡Error! El precio debe ser mayor que cero y la cantidad no puede ser negativa.")
                else:
                    inventario[product_name] = (product_value, amount_product) # We use the clue name in the diccionary.
                    break
            except ValueError:
                print("¡Error! Por favor, ingrese un precio válido (número).")
        
    return inventario

#The second option in the menu. It's function is to search any product and find out if it is in the inventary.
def consult_product(inventario):
    search_name = input("Ingrese el nombre del producto que desea consultar: ").strip()
    if search_name in inventario:
        value, amount = inventario[search_name]
        print(f"Detalles de '{search_name}': ")
        print(f"  Precio: ${value:.2f}")
        print(f"  Cantidad Disponible: {amount}")
    else:
        print(f"El producto '{search_name}' no se encuentra en el inventario.")

#This function is to update the price of any product in the inventary.
def update_price(inventario):
    name = input("Ingrese el nombre del producto cuyo precio desea actualizar: ").strip()
    if name in inventario:
        try:
            new_price = float(input(f"Ingrese el nuevo precio para '{name}': "))
            if new_price <= 0:
                print("Error, el precio debe ser mayor a 0.")
                return
            previous_price, amount = inventario[name]
            inventario[name] = (new_price, amount)
            print(f"El precio de '{name}' se ha actualizado de ${previous_price:.2f} a ${new_price:.2f}")
        except ValueError:
            print("Error, por favor ingrese un número válido para el precio.")
    else:
        print(f"El producto '{name}' no está en el inventario.")

#This function is to delete product in the inventary.
def delete_product(inventario):
    name_to_delete = input("Ingrese el nombre del producto que desea eliminar: ").strip()
    if name_to_delete in inventario:
        del inventario[name_to_delete]
        print(f"El producto '{name_to_delete}' ha sido eliminado del inventario.")
    else:
        print(f"El producto '{name_to_delete}' no está en el inventario.")

# This Lambda function is to calculate the total value in the inventary.
def calculate_total_value(inventario):
    total_value = sum(price * amount for price, amount in inventario.values())
    print(f"El valor total del inventario es ${total_value:.2f}")

#This function defines how does it look de menu of the options the user can choose.
def menu():
    print("\n---Gestión de Inventario Digital---")
    print("1. Añadir Producto")
    print("2. Consultar Producto")
    print("3. Actualizar Precio")
    print("4. Eliminar producto")
    print("5. Calcular valor total del inventario")
    print("6. Salir")

#The principal function an the order of the code flow.
def main():
    inventario = {}

    while True:
        menu()
        option = input("Seleccione una opción: ")
        if option == '1':
            inventario = Product_in(inventario) # Pasamos el inventario y actualizamos su valor
        elif option == '2':
            consult_product(inventario) # Pasamos el inventario
        elif option == '3':
            update_price(inventario) # Pasamos el inventario
        elif option == '4':
            delete_product(inventario) # Pasamos el inventario
        elif option == '5':
            calculate_total_value(inventario) # Pasamos el inventario
        elif option == '6':
            print("¡Gracias por usar el Gestor de Inventario Digital!")
            break
        else:
            print("Opción Inválida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()
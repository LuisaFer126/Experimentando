# Digital Bookstore Inventory Management System

def add_book(inventory):
    """Allows the user to add a new book to the inventory."""
    print("\nAdding a new book to the inventory:")
    title = input("Enter the title of the book: ").strip()
    while True:
        try:
            price = float(input("Enter the price of the book: "))
            if price <= 0:
                print("Error: The price must be a positive number.")
            else:
                break
        except ValueError:
            print("Error: Invalid input. Please enter a valid number for the price.")

    while True:
        try:
            quantity = int(input("Enter the quantity available: "))
            if quantity < 0:
                print("Error: The quantity cannot be negative.")
            else:
                break
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer for the quantity.")

    if title in inventory:
        print(f"Warning: A book with the title '{title}' already exists in the inventory.")
        update = input("Do you want to update its quantity? (yes/no): ").lower()
        if update == 'yes':
            inventory[title]['quantity'] += quantity
            print(f"The quantity of '{title}' has been updated to {inventory[title]['quantity']}.")
        else:
            print(f"The book '{title}' was not added.")
    else:
        inventory[title] = {'price': price, 'quantity': quantity}
        print(f"Book '{title}' has been added to the inventory.")

def consult_book(inventory):
    """Allows the user to search for a book by title and display its details."""
    print("\nConsulting a book in the inventory:")
    title_to_search = input("Enter the title of the book to search for: ").strip()
    if title_to_search in inventory:
        book = inventory[title_to_search]
        print(f"\nDetails for '{title_to_search}':")
        print(f"  Title: {title_to_search}")
        print(f"  Price: ${book['price']:.2f}")
        print(f"  Quantity: {book['quantity']}")
    else:
        print(f"Error: The book '{title_to_search}' is not found in the inventory.")

def update_price(inventory):
    """Allows the user to update the price of a specific book in the inventory."""
    print("\nUpdating the price of a book:")
    title_to_update = input("Enter the title of the book to update the price for: ").strip()
    if title_to_update in inventory:
        while True:
            try:
                new_price = float(input(f"Enter the new price for '{title_to_update}': "))
                if new_price <= 0:
                    print("Error: The price must be a positive number.")
                else:
                    inventory[title_to_update]['price'] = new_price
                    print(f"The price of '{title_to_update}' has been updated to ${new_price:.2f}.")
                    break
            except ValueError:
                print("Error: Invalid input. Please enter a valid number for the price.")
    else:
        print(f"Error: The book '{title_to_update}' is not found in the inventory.")

def delete_book(inventory):
    """Allows the user to delete a book from the inventory."""
    print("\nDeleting a book from the inventory:")
    title_to_delete = input("Enter the title of the book to delete: ").strip()
    if title_to_delete in inventory:
        confirm = input(f"Are you sure you want to delete '{title_to_delete}'? (yes/no): ").lower()
        if confirm == 'yes':
            del inventory[title_to_delete]
            print(f"Book '{title_to_delete}' has been removed from the inventory.")
        else:
            print(f"Deletion of '{title_to_delete}' cancelled.")
    else:
        print(f"Error: The book '{title_to_delete}' is not found in the inventory.")

def calculate_total_value(inventory):
    """Calculates and displays the total value of the inventory."""
    total_value = 0
    for book in inventory.values():
        total_value += book['price'] * book['quantity']
    print(f"\nThe total value of the inventory is: ${total_value:.2f}")

def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- Bookstore Inventory Management ---")
    print("1. Add Book to Inventory")
    print("2. Consult Book in Inventory")
    print("3. Update Book Price")
    print("4. Delete Book from Inventory")
    print("5. Calculate Total Inventory Value")
    print("6. Exit")
    print("------------------------------------")

def main():
    """Main function to run the bookstore inventory management system."""
    initial_inventory = {
        "The Lord of the Rings": {"price": 25.99, "quantity": 15},
        "Pride and Prejudice": {"price": 12.50, "quantity": 25},
        "To Kill a Mockingbird": {"price": 18.75, "quantity": 20},
        "1984": {"price": 15.20, "quantity": 30},
        "The Great Gatsby": {"price": 11.99, "quantity": 18}
    }
    inventory = initial_inventory

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_book(inventory)
        elif choice == '2':
            consult_book(inventory)
        elif choice == '3':
            update_price(inventory)
        elif choice == '4':
            delete_book(inventory)
        elif choice == '5':
            calculate_total_value(inventory)
        elif choice == '6':
            calculate_total_value(inventory)
            print("Exiting the Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
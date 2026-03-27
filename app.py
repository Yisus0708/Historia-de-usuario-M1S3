from inputs import read_float, read_int, read_name, read_path
from services import add_product, show_inventory, search_product, update_product, delete_product
from statistics_module import show_statistics
from files import save_csv, load_csv, merge


def option_add(inventory):
    print("\n-- Add product --")
    name = read_name("Name: ")
    price = read_float("Price: ")
    quantity = read_int("Quantity: ")
    add_product(inventory, name, price, quantity)


def option_show(inventory):
    print("\n-- Inventory --")
    show_inventory(inventory)


def option_search(inventory):
    print("\n-- Search product --")
    name = read_name("Name to search: ")
    product = search_product(inventory, name)
    if product:
        print("Name: " + product["name"])
        print("Price: " + str(product["price"]))
        print("Quantity: " + str(product["quantity"]))
    else:
        print("Product not found.")


def option_update(inventory):
    print("\n-- Update product --")
    name = read_name("Product name: ")
    if search_product(inventory, name) is None:
        print("Product not found.")
        return
    print("Leave blank to keep current value.")
    new_price = read_float("New price: ", allow_none=True)
    new_quantity = read_int("New quantity: ", allow_none=True)
    if new_price is None and new_quantity is None:
        print("No changes made.")
    else:
        update_product(inventory, name, new_price, new_quantity)


def option_delete(inventory):
    print("\n-- Delete product --")
    name = read_name("Name to delete: ")
    if search_product(inventory, name) is None:
        print("Product not found.")
        return
    confirm = input("Confirm deletion of " + name + " (yes/no): ").strip()
    if confirm == "yes" or confirm == "Yes":
        delete_product(inventory, name)
    else:
        print("Operation cancelled.")


def option_statistics(inventory):
    show_statistics(inventory)


def option_save(inventory):
    print("\n-- Save CSV --")
    path = read_path("File path (e.g. inventory.csv): ")
    save_csv(inventory, path)


def option_load(inventory):
    print("\n-- Load CSV --")
    path = read_path("File path to load: ")
    new_products, invalid_rows = load_csv(path)

    if not new_products:
        if invalid_rows > 0:
            print("No products loaded. Invalid rows: " + str(invalid_rows))
        return

    print("Valid products found: " + str(len(new_products)))
    if invalid_rows > 0:
        print("Invalid rows skipped: " + str(invalid_rows))

    action = input("Overwrite current inventory? (yes/no): ").strip()

    if action == "yes" or action == "Yes":
        inventory.clear()
        inventory.extend(new_products)
        print("Inventory replaced.")
    else:
        summary = merge(inventory, new_products)
        print("Added: " + str(summary["added"]))
        print("Updated: " + str(summary["updated"]))

    show_inventory(inventory)


def show_menu():
    print("\nINVENTORY SYSTEM")
    print("1. Add product")
    print("2. Show inventory")
    print("3. Search product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Statistics")
    print("7. Save CSV")
    print("8. Load CSV")
    print("9. Exit")


def main():
    inventory = []
    print("Welcome to the Inventory System")
    running = True

    while running:
        show_menu()
        option = input("Select an option (1-9): ").strip()

        if option == "1":
            option_add(inventory)
        elif option == "2":
            option_show(inventory)
        elif option == "3":
            option_search(inventory)
        elif option == "4":
            option_update(inventory)
        elif option == "5":
            option_delete(inventory)
        elif option == "6":
            option_statistics(inventory)
        elif option == "7":
            option_save(inventory)
        elif option == "8":
            option_load(inventory)
        elif option == "9":
            print("Goodbye.")
            running = False
        else:
            print("Invalid option. Enter a number from 1 to 9.")


if __name__ == "__main__":
    main()

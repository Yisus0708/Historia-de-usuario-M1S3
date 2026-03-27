def add_product(inventory, name, price, quantity):
    if search_product(inventory, name) is not None:
        print("Product " + name + " already exists.")
        return False
    product = {"name": name.strip(), "price": float(price), "quantity": int(quantity)}
    inventory.append(product)
    print("Product " + name + " added successfully.")
    return True


def show_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
        return
    print("\nName | Price | Quantity")
    print("-" * 35)
    for product in inventory:
        print(product["name"] + " | " + str(product["price"]) + " | " + str(product["quantity"]))
    print("-" * 35)
    print("Total products: " + str(len(inventory)))


def search_product(inventory, name):
    for product in inventory:
        if product["name"].lower() == name.strip().lower():
            return product
    return None


def update_product(inventory, name, new_price=None, new_quantity=None):
    product = search_product(inventory, name)
    if product is None:
        print("Product " + name + " not found.")
        return False
    if new_price is not None:
        product["price"] = float(new_price)
    if new_quantity is not None:
        product["quantity"] = int(new_quantity)
    print("Product " + name + " updated.")
    return True


def delete_product(inventory, name):
    product = search_product(inventory, name)
    if product is None:
        print("Product " + name + " not found.")
        return False
    inventory.remove(product)
    print("Product " + name + " deleted.")
    return True

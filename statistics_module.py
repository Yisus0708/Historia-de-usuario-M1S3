def calculate_statistics(inventory):
    if not inventory:
        return None

    total_units = 0
    total_value = 0
    most_expensive = inventory[0]
    highest_stock = inventory[0]

    for product in inventory:
        total_units += product["quantity"]
        total_value += product["price"] * product["quantity"]
        if product["price"] > most_expensive["price"]:
            most_expensive = product
        if product["quantity"] > highest_stock["quantity"]:
            highest_stock = product

    return {
        "total_units": total_units,
        "total_value": total_value,
        "most_expensive_product": (most_expensive["name"], most_expensive["price"]),
        "highest_stock_product": (highest_stock["name"], highest_stock["quantity"]),
    }


def show_statistics(inventory):
    stats = calculate_statistics(inventory)
    if stats is None:
        print("Inventory is empty, no statistics available.")
        return

    expensive_name, expensive_price = stats["most_expensive_product"]
    stock_name, stock_qty = stats["highest_stock_product"]

    print("\nInventory statistics:")
    print("Total units: " + str(stats["total_units"]))
    print("Total value: " + str(round(stats["total_value"], 2)))
    print("Most expensive: " + expensive_name + " (" + str(expensive_price) + ")")
    print("Most stock: " + stock_name + " (" + str(stock_qty) + " units)")

    print("\nSubtotal per product:")
    for product in inventory:
        subtotal = product["price"] * product["quantity"]
        print(product["name"] + ": " + str(round(subtotal, 2)))

import csv

HEADER = ["name", "price", "quantity"]


def save_csv(inventory, path, include_header=True):
    if not inventory:
        print("Inventory is empty. Nothing to save.")
        return False

    try:
        file = open(path, "w", newline="", encoding="utf-8")
        writer = csv.DictWriter(file, fieldnames=HEADER)
        if include_header:
            writer.writeheader()
        for product in inventory:
            writer.writerow({
                "name": product["name"],
                "price": product["price"],
                "quantity": product["quantity"],
            })
        file.close()
        print("Inventory saved to: " + path)
        return True

    except PermissionError:
        print("No permission to write to " + path)
    except OSError as e:
        print("Error saving file: " + str(e))
    except Exception as e:
        print("Unexpected error while saving: " + str(e))

    return False


def load_csv(path):
    products = []
    invalid_rows = 0

    try:
        file = open(path, "r", newline="", encoding="utf-8")
        reader = csv.reader(file)

        header = next(reader)
        header_norm = []
        for col in header:
            header_norm.append(col.strip().lower())

        if header_norm != HEADER:
            print("Invalid header. Expected: name,price,quantity")
            file.close()
            return [], 0

        row_num = 2
        for row in reader:
            if len(row) != 3:
                print("Row " + str(row_num) + ": incorrect columns. Skipped.")
                invalid_rows += 1
                row_num += 1
                continue

            name_val = row[0].strip()
            price_val = row[1]
            quantity_val = row[2]

            if not name_val:
                print("Row " + str(row_num) + ": empty name. Skipped.")
                invalid_rows += 1
                row_num += 1
                continue

            try:
                price_num = float(price_val)
                if price_num < 0:
                    print("Row " + str(row_num) + ": negative price. Skipped.")
                    invalid_rows += 1
                    row_num += 1
                    continue
            except ValueError:
                print("Row " + str(row_num) + ": invalid price. Skipped.")
                invalid_rows += 1
                row_num += 1
                continue

            try:
                quantity_num = int(float(quantity_val))
                if quantity_num < 0:
                    print("Row " + str(row_num) + ": negative quantity. Skipped.")
                    invalid_rows += 1
                    row_num += 1
                    continue
            except ValueError:
                print("Row " + str(row_num) + ": invalid quantity. Skipped.")
                invalid_rows += 1
                row_num += 1
                continue

            product = {"name": name_val, "price": price_num, "quantity": quantity_num}
            products.append(product)
            row_num += 1

        file.close()

    except FileNotFoundError:
        print("File not found: " + path)
        return [], 0
    except UnicodeDecodeError:
        print("File has incompatible characters.")
        return [], 0
    except Exception as e:
        print("Unexpected error while loading: " + str(e))
        return [], 0

    return products, invalid_rows


def merge(current_inventory, new_products):
    print("Merge policy:")
    print("  - New name: added to inventory.")
    print("  - Existing name: quantity is added and price updated if different.")

    added = 0
    updated = 0

    for new in new_products:
        found = None
        for product in current_inventory:
            if product["name"].lower() == new["name"].lower():
                found = product
        if found is None:
            current_inventory.append(new)
            added += 1
        else:
            found["quantity"] += new["quantity"]
            if found["price"] != new["price"]:
                found["price"] = new["price"]
            updated += 1

    return {"added": added, "updated": updated}

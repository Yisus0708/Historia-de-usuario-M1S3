def read_float(message, allow_none=False):
    value = None
    valid = False
    while not valid:
        entry = input(message).strip()
        if allow_none and entry == "":
            return None
        try:
            value = float(entry)
            if value < 0:
                print("Value cannot be negative.")
            else:
                valid = True
        except ValueError:
            print("Enter a valid number.")
    return value


def read_int(message, allow_none=False):
    value = None
    valid = False
    while not valid:
        entry = input(message).strip()
        if allow_none and entry == "":
            return None
        try:
            value = int(entry)
            if value < 0:
                print("Value cannot be negative.")
            else:
                valid = True
        except ValueError:
            print("Enter a valid integer.")
    return value


def read_name(message):
    name = ""
    valid = False
    while not valid:
        name = input(message).strip()
        if name:
            valid = True
        else:
            print("Name cannot be empty.")
    return name


def read_path(message):
    path = ""
    valid = False
    while not valid:
        path = input(message).strip()
        if path:
            valid = True
        else:
            print("Path cannot be empty.")
    return path

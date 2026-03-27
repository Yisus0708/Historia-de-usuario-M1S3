Inventory Management System (CLI)

📌 Description

This is a simple command-line inventory management system built in Python.
It allows users to manage products, including adding, updating, deleting, searching, and storing inventory data using CSV files.

---

🚀 Features

* Add new products
* View inventory list
* Search for a product
* Update product information
* Delete products
* View inventory statistics
* Save inventory to CSV
* Load inventory from CSV
* Merge inventories intelligently

---

🗂️ Project Structure

app.py              # Main application (menu and flow control)
servicios.py        # Core inventory operations (CRUD)
entradas.py         # Input validation utilities
archivos.py         # CSV file handling (save/load/merge)
estadisticas.py     # Inventory statistics

---

▶️ How to Run

1. Make sure you have Python installed (Python 3 recommended).
2. Run the application:

python app.py

---

📋 Menu Options

1. Add product
2. Show inventory
3. Search product
4. Update product
5. Delete product
6. Statistics
7. Save CSV
8. Load CSV
9. Exit

---

📊 Data Structure

Each product is stored as a dictionary:

{
    "nombre": str,
    "precio": float,
    "cantidad": int
}

---

💾 CSV Format

The system expects CSV files with the following header:

nombre,precio,cantidad

Example:

Apple,1.5,10
Banana,0.8,20

---

🔄 Merge Policy

When loading a CSV without overwriting:

* New products → Added
* Existing products → Quantity is increased
* Price → Updated if different

---

📈 Statistics Included

* Total units in inventory
* Total inventory value
* Most expensive product
* Product with highest stock
* Subtotal per product

---

⚠️ Error Handling

The system handles:

* Invalid inputs
* Negative values
* Incorrect CSV format
* File permission errors
* Missing files

---

🧠 Notes

* All inputs are validated before processing.
* Product names are case-insensitive when searching.
* Empty inventory prevents saving to CSV.

---

🖼️ Diagram

<img width="3632" height="1796" alt="Historial de usario drawio (1)" src="https://github.com/user-attachments/assets/3a0c6cc0-7dd2-4964-bfb1-2c038d4b17d2" />




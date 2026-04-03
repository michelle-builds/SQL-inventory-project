# SQL project for Github

import sqlite3

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT,
        price REAL,
        quantity INTEGER,
        supplier TEXT
    )
""")
conn.commit()
print("Table created.")

cursor.execute("SELECT COUNT(*) FROM products")
if cursor.fetchone()[0] == 0:
    cursor.execute("INSERT INTO products (name, category, price, quantity, supplier) VALUES ('Apples', 'Produce', 1.99, 50, 'Fresh Farms')")
    cursor.execute("INSERT INTO products (name, category, price, quantity, supplier) VALUES ('Milk', 'Dairy', 4.49, 30, 'Dairyland')")
    cursor.execute("INSERT INTO products (name, category, price, quantity, supplier) VALUES ('Bread', 'Bakery', 3.29, 40, 'Wonder')")
    cursor.execute("INSERT INTO products (name, category, price, quantity, supplier) VALUES ('Cheddar', 'Dairy', 6.99, 20, 'Dairyland')")
    cursor.execute("INSERT INTO products (name, category, price, quantity, supplier) VALUES ('Chicken', 'Meat', 12.99, 15, 'Maple Leaf')")
    cursor.execute("INSERT INTO products (name, category, price, quantity, supplier) VALUES ('Carrots', 'Produce', 1.49, 60, 'Fresh Farms')")
    conn.commit()

# View all products
print("\n=== ALL PRODUCTS ===")
cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Low stock
print("\n=== LOW STOCK (under 25 units) ===")
cursor.execute("SELECT name, category, quantity FROM products WHERE quantity < 25")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Average price by category
print("\n=== AVERAGE PRICE BY CATEGORY ===")
cursor.execute("SELECT category, AVG(price) FROM products GROUP BY category")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Total inventory value
print("\n=== TOTAL INVENTORY VALUE ===")
cursor.execute("SELECT SUM(price * quantity) FROM products")
row = cursor.fetchone()
print(f"Total value: ${row[0]:.2f}")    
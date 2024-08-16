import sqlite3

conn = sqlite3.connect('billing.db')
c = conn.cursor()

# tables for products and customers
c.execute('''CREATE TABLE IF NOT EXISTS products (
             product_id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             price REAL NOT NULL)''')

c.execute('''CREATE TABLE IF NOT EXISTS customers (
             customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             phone TEXT NOT NULL)''')

c.execute('''CREATE TABLE IF NOT EXISTS invoices (
             invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
             customer_id INTEGER,
             date TEXT NOT NULL,
             FOREIGN KEY(customer_id) REFERENCES customers(customer_id))''')

c.execute('''CREATE TABLE IF NOT EXISTS invoice_items (
             item_id INTEGER PRIMARY KEY AUTOINCREMENT,
             invoice_id INTEGER,
             product_id INTEGER,
             quantity INTEGER NOT NULL,
             FOREIGN KEY(invoice_id) REFERENCES invoices(invoice_id),
             FOREIGN KEY(product_id) REFERENCES products(product_id))''')

conn.commit()
conn.close()

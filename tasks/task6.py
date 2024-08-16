import sqlite3
from tkinter import *
from tkinter import messagebox

conn = sqlite3.connect('billing.db')
c = conn.cursor()

root = Tk()
root.title("Billing Software")

# Global variables
cart = []

# Add product to the database
def add_product():
    name = entry_product_name.get()
    price = float(entry_product_price.get())

    c.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
    conn.commit()
    messagebox.showinfo("Success", "Product added successfully!")
    entry_product_name.delete(0, END)
    entry_product_price.delete(0, END)

# Add customer to the database
def add_customer():
    name = entry_customer_name.get()
    phone = entry_customer_phone.get()

    c.execute("INSERT INTO customers (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()
    messagebox.showinfo("Success", "Customer added successfully!")
    entry_customer_name.delete(0, END)
    entry_customer_phone.delete(0, END)

# Add item to the cart
def add_to_cart():
    product_id = int(entry_product_id.get())
    quantity = int(entry_quantity.get())
    
    c.execute("SELECT * FROM products WHERE product_id=?", (product_id,))
    product = c.fetchone()

    if product:
        cart.append((product_id, product[1], product[2], quantity))
        update_cart_listbox()
    else:
        messagebox.showerror("Error", "Product not found!")

# Update cart listbox
def update_cart_listbox():
    cart_listbox.delete(0, END)
    for item in cart:
        cart_listbox.insert(END, f"{item[1]} - {item[3]} x ${item[2]}")

# Generate invoice
def generate_invoice():
    customer_id = int(entry_customer_id.get())
    c.execute("INSERT INTO invoices (customer_id, date) VALUES (?, date('now'))", (customer_id,))
    invoice_id = c.lastrowid

    for item in cart:
        c.execute("INSERT INTO invoice_items (invoice_id, product_id, quantity) VALUES (?, ?, ?)",
                  (invoice_id, item[0], item[3]))
    
    conn.commit()
    messagebox.showinfo("Success", "Invoice generated successfully!")
    cart.clear()
    update_cart_listbox()

# Widgets for product
label_product_name = Label(root, text="Product Name")
label_product_name.grid(row=0, column=0)
entry_product_name = Entry(root)
entry_product_name.grid(row=0, column=1)

label_product_price = Label(root, text="Product Price")
label_product_price.grid(row=1, column=0)
entry_product_price = Entry(root)
entry_product_price.grid(row=1, column=1)

btn_add_product = Button(root, text="Add Product", command=add_product)
btn_add_product.grid(row=2, column=0, columnspan=2)

# Widgets for customer
label_customer_name = Label(root, text="Customer Name")
label_customer_name.grid(row=3, column=0)
entry_customer_name = Entry(root)
entry_customer_name.grid(row=3, column=1)

label_customer_phone = Label(root, text="Customer Phone")
label_customer_phone.grid(row=4, column=0)
entry_customer_phone = Entry(root)
entry_customer_phone.grid(row=4, column=1)

btn_add_customer = Button(root, text="Add Customer", command=add_customer)
btn_add_customer.grid(row=5, column=0, columnspan=2)

# Widgets for cart
label_product_id = Label(root, text="Product ID")
label_product_id.grid(row=6, column=0)
entry_product_id = Entry(root)
entry_product_id.grid(row=6, column=1)

label_quantity = Label(root, text="Quantity")
label_quantity.grid(row=7, column=0)
entry_quantity = Entry(root)
entry_quantity.grid(row=7, column=1)

btn_add_to_cart = Button(root, text="Add to Cart", command=add_to_cart)
btn_add_to_cart.grid(row=8, column=0, columnspan=2)

# Cart listbox
cart_listbox = Listbox(root, width=40, height=10)
cart_listbox.grid(row=9, column=0, columnspan=2)

# Generate invoice button
label_customer_id = Label(root, text="Customer ID")
label_customer_id.grid(row=10, column=0)
entry_customer_id = Entry(root)
entry_customer_id.grid(row=10, column=1)

btn_generate_invoice = Button(root, text="Generate Invoice", command=generate_invoice)
btn_generate_invoice.grid(row=11, column=0, columnspan=2)

root.mainloop()

# Close the connection
conn.close()

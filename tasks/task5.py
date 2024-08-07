import tkinter as tk
from tkinter import ttk
import requests
import csv


def load_currency_data(csv_file):
    currency_data = {}
    with open(csv_file, mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            currency_code = row["currency code"]
            currency_name = row["currency name"]
            currency_data[currency_name] = currency_code
    return currency_data


def convert_currency_rate():
    api_key = "CMSMLSO00Q9XYGBL"
    from_currency_name = from_currency_var.get()
    to_currency_name = to_currency_var.get()

    # Get the corresponding currency codes
    from_currency = currency_data[from_currency_name]
    to_currency = currency_data[to_currency_name]

    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    # Extract exchange rate and last refreshed time
    exchange_rate = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    last_refreshed = data["Realtime Currency Exchange Rate"]["6. Last Refreshed"]

    # Update labels with the exchange rate and last refreshed time
    result_label.config(
        text=f"1 {from_currency} ({from_currency_name}) = {exchange_rate} {to_currency} ({to_currency_name})"
    )
    last_refreshed_label.config(text=f"Last Refreshed: {last_refreshed}")


# Setting up the GUI window
root = tk.Tk()
root.title("Currency Exchange Rate")

# Load currency data from the CSV file
csv_file = "tasks\data\physical_currency_list.csv"
currency_data = load_currency_data(csv_file)

# Dropdowns for selecting currencies by name
from_currency_var = tk.StringVar()
to_currency_var = tk.StringVar()

from_currency_label = ttk.Label(root, text="From Currency:")
from_currency_label.pack(pady=5)

from_currency_dropdown = ttk.Combobox(root, textvariable=from_currency_var)
from_currency_dropdown["values"] = list(currency_data.keys())  # Show names only
from_currency_dropdown.pack(pady=5)

to_currency_label = ttk.Label(root, text="To Currency:")
to_currency_label.pack(pady=5)

to_currency_dropdown = ttk.Combobox(root, textvariable=to_currency_var)
to_currency_dropdown["values"] = list(currency_data.keys())  # Show names only
to_currency_dropdown.pack(pady=5)

# Button to get exchange rate
get_rate_button = ttk.Button(
    root, text="Get Exchange Rate", command=convert_currency_rate
)
get_rate_button.pack(pady=10)

# Label to show the result
result_label = ttk.Label(root, text="")
result_label.pack(pady=20)

# Label to show last refreshed time
last_refreshed_label = ttk.Label(root, text="")
last_refreshed_label.pack(pady=5)

# Run the GUI loop
root.mainloop()

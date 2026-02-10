import sqlite3
import pandas as pd

db_path = "/path/to/chinook.db"

with sqlite3.connect(db_path) as conn:
    customers = pd.read_sql("SELECT * FROM customers", conn)
    invoices = pd.read_sql("SELECT * FROM invoices", conn)

# Inner join on CustomerId
merged = customers.merge(invoices, on="CustomerId", how="inner")

# Total number of invoices per customer
invoice_counts = (
    merged.groupby("CustomerId")
          .size()
          .reset_index(name="TotalInvoices")
)

print(invoice_counts)

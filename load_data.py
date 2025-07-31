import pandas as pd
import sqlite3

# Load CSV
df = pd.read_csv("data/products.csv")

# Connect to DB
conn = sqlite3.connect("ecommerce.db")

# Insert data
df.to_sql("products", conn, if_exists="append", index=False)

conn.close()
print("✅ Data loaded successfully.")

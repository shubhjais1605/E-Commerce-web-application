import sqlite3

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM products LIMIT 5")
rows = cursor.fetchall()

print("📦 Sample Products:")
for row in rows:
    print(row)

conn.close()

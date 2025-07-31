import sqlite3

def create_products_table():
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            title TEXT,
            price REAL,
            discounted_price REAL,
            image TEXT,
            description TEXT,
            category TEXT,
            subcategory TEXT,
            brand TEXT
        )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_products_table()

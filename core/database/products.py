import sqlite3 as sq


async def db_start():
    try:
        db = sq.connect('products.db')
        cur = db.cursor()

        cur.execute('CREATE TABLE IF NOT EXISTS product('
                    'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                    'name TEXT, description TEXT, photo TEXT, price TEXT, category TEXT, brand TEXT)')

        db.commit()
        print('db start')
        return db, cur
    except Exception as e:
        print("Error during database initialization:", str(e))
        return None, None


async def create_product(name, description, photo, category, brand, price):
    db = sq.connect('products.db')
    cur = db.cursor()
    cur.execute("INSERT INTO product (name, description, photo, price, category, brand) VALUES (?, ?, ?, ?, ?, ?)",
                (name, description, photo, price, category, brand))
    cur.connection.commit()
    cur.close()


async def get_products(cur):
    cur.execute("SELECT * FROM product")
    products = cur.fetchall()
    return products

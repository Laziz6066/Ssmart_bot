import sqlite3 as sq


async def db_start_order():
    try:
        db = sq.connect('order.db')
        cur = db.cursor()

        cur.execute('CREATE TABLE IF NOT EXISTS orders ('
                    'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                    'name TEXT, phone TEXT, product_name TEXT, product_price TEXT)')

        db.commit()
        print('db start')
        return db, cur
    except Exception as e:
        print("Error during database initialization:", str(e))
        return None, None


async def create_order(name, phone, product_name, product_price):
    db = sq.connect('order.db')
    cur = db.cursor()
    cur.execute("INSERT INTO orders(name, phone, product_name, product_price) VALUES (?, ?, ?, ?)",
                (name, phone, product_name, product_price))
    cur.connection.commit()
    cur.close()


async def get_orders(cur):
    cur.execute("SELECT * FROM orders")
    orders = cur.fetchall()
    return orders

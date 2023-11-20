import sqlite3 as sq


async def db_start_mailing():
    try:
        db = sq.connect('mailing.db')
        cur = db.cursor()

        cur.execute('CREATE TABLE IF NOT EXISTS mailings ('
                    'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                    'description TEXT, photo TEXT)')

        db.commit()
        print('db start')
        return db, cur
    except Exception as e:
        print("Error during database initialization:", str(e))
        return None, None


async def create_mailing(description, photo):
    db = sq.connect('mailing.db')
    cur = db.cursor()
    cur.execute("INSERT INTO mailings(description, photo) VALUES (?, ?)",
                (description, photo))
    cur.connection.commit()
    cur.close()


async def get_mailings(cur):
    cur.execute("SELECT * FROM mailings")
    mailings = cur.fetchall()
    return mailings

import sqlite3 as sq


async def db_start_language():
    try:
        db = sq.connect('language.db')
        cur = db.cursor()

        cur.execute('CREATE TABLE IF NOT EXISTS language('
                    'user_id INTEGER PRIMARY KEY, '
                    'lang TEXT)')

        db.commit()
        print('db lang start')
        return db, cur
    except Exception as e:
        print("Error during database initialization:", str(e))
        return None, None


async def create_language(user_id, lang):
    db, cur = await db_start_language()
    cur.execute("INSERT OR REPLACE INTO language (user_id, lang) VALUES (?, ?)", (user_id, lang))
    db.commit()
    cur.close()


async def get_language(user_id):
    db, cur = await db_start_language()
    cur.execute("SELECT lang FROM language WHERE user_id=?", (user_id,))
    lang = cur.fetchone()
    cur.close()
    return lang[0] if lang else None


async def get_user_id(cur):
    cur.execute("SELECT * FROM language")
    mailings = cur.fetchall()
    return mailings

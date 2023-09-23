import sqlite3


db = sqlite3.connect('database/bot.db')
cur = db.cursor()


async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS accounts("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "cart_id TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS items("
                "i_id id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "name TEXT,"
                "low TEXT)")
    db.commit()
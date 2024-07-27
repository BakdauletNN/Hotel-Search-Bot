import sqlite3
from datetime import datetime


db = sqlite3.connect('database/bot.db', check_same_thread=False)
cur = db.cursor()


def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS accounts("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "cart_id TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS items("
                "i_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "name TEXT,"
                "low TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS history("
                "user_id INTEGER,"
                "command TEXT,"
                "city TEXT,"
                "entry_date TEXT,"
                "exit_date TEXT,"
                "adults INTEGER,"
                "children TEXT,"
                "location_id TEXT,"
                "hotels_qty INTEGER,"
                "photos INTEGER,"
                "min_price REAL,"
                "max_price REAL,"
                "distance_from_center REAL,"
                "request_date TEXT)")
    db.commit()


def add_history(user_id, command, city, entry_date, exit_date, adults, children, location_id, hotels_qty, photos, min_price, max_price, distance_from_center):
    request_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cur.execute("INSERT INTO history (user_id, command, city, entry_date, exit_date, adults, children, location_id, hotels_qty, photos, min_price, max_price, distance_from_center, request_date) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (user_id, command, city, entry_date, exit_date, adults, children, location_id, hotels_qty, photos, min_price, max_price, distance_from_center, request_date))
    db.commit()


def get_history(user_id):
    cur.execute("SELECT * FROM history WHERE user_id = ?", (user_id,))
    return cur.fetchall()


db_start()

# import sqlite3
#
#
# db = sqlite3.connect('database/bot.db', check_same_thread=False)
# cur = db.cursor()
#
#
# def db_start():
#     cur.execute("CREATE TABLE IF NOT EXISTS history("
#                 "user_id INTEGER,"
#                 "command TEXT,"
#                 "location_id TEXT,"
#                 "city TEXT,"
#                 "adults INTEGER,"
#                 "children TEXT,"
#                 "entry_date date,"
#                 "exit_date date,"
#                 "hotels_qty INTEGER,"
#                 "photos INTEGER,"
#                 "min_price REAL,"
#                 "max_price REAL,"
#                 "distance_from_center REAL,"
#                 "request_date TEXT)")
#     db.commit()

import sqlite3 as sqlite


DB_NAME = "users.db"

conn = sqlite.connect(DB_NAME)

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS user
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        email TEXT NOT NULL,
        password TEXT NOT NULL, 
        name TEXT NOT NULL,
        address TEXT NOT NULL,
        phone_number INTEGER
    )
''')

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS ad
    ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        price REAL,
        date TEXT NOT NULL,
        is_active INTEGER,
        owner_id INTEGER,
        buyer_id INTEGER,
        FOREIGN KEY(owner_id) REFERENCES user(id)
    )
''')

conn.commit()


class SQLite(object):
    def __enter__(self):
        self.conn = sqlite.connect(DB_NAME)
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()

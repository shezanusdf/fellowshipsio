import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE fellowships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    organization TEXT NOT NULL,
    description TEXT,
    website TEXT,
    deadline TEXT,
    type TEXT,
    region TEXT,
    tags TEXT
)
""")

connection.commit()

print(cursor.fetchall())

connection.close()
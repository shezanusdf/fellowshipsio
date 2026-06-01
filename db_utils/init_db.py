import sqlite3
import os

DB_PATH = os.environ.get("DATABASE_PATH", "database.db")

connection = sqlite3.connect(DB_PATH)

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
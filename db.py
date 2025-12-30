import sqlite3

conn = sqlite3.connect("todo.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Database and tasks table created successfully!")

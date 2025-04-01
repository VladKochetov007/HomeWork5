import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

try:
    cursor.execute("CREATE TABLE students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, male BOOLEAN, birth_date DATE)")
except sqlite3.OperationalError:
    pass

def soon_birthday(db: sqlite3.Connection, days: int = 2) -> bool:
    today = datetime.now()
    cursor.execute("SELECT * FROM students WHERE birth_date >= ? AND birth_date <= ?", (today, today + timedelta(days=days)))
    return cursor.fetchall()

def add_student(db: sqlite3.Connection, name: str, age: int, male: bool, birth_date: str):
    cursor.execute("INSERT INTO students (name, age, male, birth_date) VALUES (?, ?, ?, ?)", (name, age, male, birth_date))
    db.commit()

if __name__ == "__main__":
    add_student(conn, "Boobaaa", 41, False, "2025-04-05")

    print("---")

    print(soon_birthday(conn, 2))
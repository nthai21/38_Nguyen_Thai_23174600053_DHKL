import sqlite3
def create_table_and_insert_records():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    ''')

    users = [
        (1, 'Alice', 30),
        (2, 'Bob', 25),
        (3, 'Charlie', 35)
    ]
    cursor.executemany('INSERT OR IGNORE INTO users (id, name, age) VALUES (?, ?, ?)', users)

    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()

    print("Danh sách các bản ghi trong bảng 'users':")
    for row in rows:
        print(row)

    conn.commit()
    conn.close()

create_table_and_insert_records()

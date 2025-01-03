import sqlite3
def count_records():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM users')
    count = cursor.fetchone()[0]

    print(f"Số bản ghi trong bảng 'users': {count}")

    conn.close()

count_records()
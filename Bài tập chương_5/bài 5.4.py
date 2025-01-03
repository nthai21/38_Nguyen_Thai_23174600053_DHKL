import sqlite3
def list_tables():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()

    print("Danh sách các bảng trong cơ sở dữ liệu:")
    for table in tables:
        print(f"- {table[0]}")

    conn.close()

list_tables()
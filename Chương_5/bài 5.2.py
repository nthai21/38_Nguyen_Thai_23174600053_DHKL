import sqlite3
def connect_to_memory_database():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('SELECT sqlite_version()')
    version = cursor.fetchone()

    print(f"SQLite Version (In-Memory): {version[0]}")
    conn.close()

connect_to_memory_database()
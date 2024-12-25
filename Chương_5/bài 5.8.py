import sqlite3
def delete_specific_row():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    row_id = input("Nhập ID của hàng cần xóa: ")

    cursor.execute('DELETE FROM users WHERE id = ?', (row_id,))

    if cursor.rowcount > 0:
        print(f"Đã xóa thành công hàng có ID = {row_id}.")
    else:
        print(f"Không tìm thấy hàng có ID = {row_id}.")

    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    print("Danh sách các bản ghi còn lại:")
    for row in rows:
        print(row)

    conn.commit()
    conn.close()

delete_specific_row()

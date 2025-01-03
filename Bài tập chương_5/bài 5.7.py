import sqlite3
def update_column_values():

    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

 
    new_value = input("Nhập giá trị mới cho cột age: ")

   
    cursor.execute('UPDATE users SET age = ?', (new_value,))

    print(f"Cập nhật tất cả các giá trị của cột 'age' thành {new_value} thành công.")


    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    print("Danh sách các bản ghi sau khi cập nhật:")
    for row in rows:
        print(row)

    conn.commit()
    conn.close()


update_column_values()

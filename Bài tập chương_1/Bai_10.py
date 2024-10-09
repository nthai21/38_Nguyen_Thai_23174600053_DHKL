import math

class Diem:
    def __init__(self, x=0, y=0):
        self.x = x 
        self.y = y 

class Elip(Diem):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)  # Gọi hàm khởi tạo lớp điểm
        self.a = a 
        self.b = b  

    def dien_tich(self):
        return math.pi * self.a * self.b  

class DuongTron(Elip):
    def __init__(self, x, y, ban_kinh):
        super().__init__(x, y, ban_kinh, ban_kinh)  
        self.ban_kinh = ban_kinh

    def dien_tich(self):
        return math.pi * self.ban_kinh ** 2  


if __name__ == "__main__":
    elip = Elip(0, 0, 5, 3) 
    print(f"Diện tích elip: {elip.dien_tich()}")

    duong_tron = DuongTron(0, 0, 4)  
    print(f"Diện tích đường tròn: {duong_tron.dien_tich()}")

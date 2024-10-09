import math

class TamGiac:
    def __init__(self, canh1, canh2, canh3):
        self.canh1 = canh1  
        self.canh2 = canh2  
        self.canh3 = canh3  

    def chu_vi(self):
        return self.canh1 + self.canh2 + self.canh3  

    def dien_tich(self):
        p = self.chu_vi() / 2
        return math.sqrt(p * (p - self.canh1) * (p - self.canh2) * (p - self.canh3))


class TamGiacVuong(TamGiac):
    def __init__(self, canh1, canh2):
        super().__init__(canh1, canh2, math.sqrt(canh1**2 + canh2**2))  # Cạnh huyền

    def dien_tich(self):
        return 0.5 * self.canh1 * self.canh2  


class TamGiacCan(TamGiac):
    def __init__(self, canh_bang, canh_khac):
        super().__init__(canh_bang, canh_bang, canh_khac) 


class TamGiacDeu(TamGiacCan):
    def __init__(self, canh):
        super().__init__(canh, canh)  # Tất cả các cạnh bằng nhau


if __name__ == "__main__":
    tam_giac = TamGiac(3, 4, 5)
    print(f"Chu vi tam giác: {tam_giac.chu_vi()}")
    print(f"Diện tích tam giác: {tam_giac.dien_tich()}")

    tam_giac_vuong = TamGiacVuong(3, 4)
    print(f"Chu vi tam giác vuông: {tam_giac_vuong.chu_vi()}")
    print(f"Diện tích tam giác vuông: {tam_giac_vuong.dien_tich()}")

    tam_giac_can = TamGiacCan(5, 8)
    print(f"Chu vi tam giác cân: {tam_giac_can.chu_vi()}")
    print(f"Diện tích tam giác cân: {tam_giac_can.dien_tich()}")

    tam_giac_deu = TamGiacDeu(6)
    print(f"Chu vi tam giác đều: {tam_giac_deu.chu_vi()}")
    print(f"Diện tích tam giác đều: {tam_giac_deu.dien_tich()}")

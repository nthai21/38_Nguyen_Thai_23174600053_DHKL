class DaGiac:
    def __init__(self, so_canh):
        self.so_canh = so_canh

    def chu_vi(self):
        raise NotImplementedError("Phương thức này chưa được định nghĩa.")


class HinhBinhHanh(DaGiac):
    def __init__(self, day, cao):
        super().__init__(4)  # Hình bình hành có 4 cạnh
        self.day = day
        self.cao = cao

    def dien_tich(self):
        return self.day * self.cao

    def chu_vi(self):
        return 2 * (self.day + self.cao)


class HinhChuNhat(HinhBinhHanh):
    def __init__(self, rong, cao):
        super().__init__(rong, cao)
        self.rong = rong

    def dien_tich(self):
        return self.rong * self.cao


class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)

if __name__ == "__main__":
    hinh_vuong = HinhVuong(4)
    print(f"Chu vi hình vuông: {hinh_vuong.chu_vi()}")
    print(f"Diện tích hình vuông: {hinh_vuong.dien_tich()}")

    hinh_chu_nhat = HinhChuNhat(5, 3)
    print(f"Chu vi hình chữ nhật: {hinh_chu_nhat.chu_vi()}")
    print(f"Diện tích hình chữ nhật: {hinh_chu_nhat.dien_tich()}")

    hinh_binh_hanh = HinhBinhHanh(6, 4)
    print(f"Chu vi hình bình hành: {hinh_binh_hanh.chu_vi()}")
    print(f"Diện tích hình bình hành: {hinh_binh_hanh.dien_tich()}")

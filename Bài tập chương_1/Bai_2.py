class TS:
    def __init__(self, ho_ten="", diem_toan=0, diem_ly=0, diem_hoa=0):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ tên thí sinh: ")
        self.diem_toan = float(input("Nhập điểm Toán: "))
        self.diem_ly = float(input("Nhập điểm Lý: "))
        self.diem_hoa = float(input("Nhập điểm Hoá: "))

    def in_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Điểm Toán: {self.diem_toan}, Điểm Lý: {self.diem_ly}, Điểm Hoá: {self.diem_hoa}")
        print(f"Tổng điểm: {self.tinh_tong_diem()}")

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa
#--------------------------------------------------------------
if __name__ == "__main__":
    danh_sach_thi_sinh = []
    so_thi_sinh = int(input("Nhập số lượng thí sinh: "))

    for _ in range(so_thi_sinh):
        ts = TS()
        ts.nhap_thong_tin()
        danh_sach_thi_sinh.append(ts)

    # Lọc thí sinh trúng tuyển
    diem_chuan = 20
    thi_sinh_trung_tuyen = [ts for ts in danh_sach_thi_sinh if ts.tinh_tong_diem() >= diem_chuan]

    # Sắp xếp theo điểm từ cao xuống thấp
    thi_sinh_trung_tuyen.sort(key=lambda x: x.tinh_tong_diem(), reverse=True)

    # In danh sách thí sinh trúng tuyển
    print("\nDanh sách thí sinh trúng tuyển:")
    for ts in thi_sinh_trung_tuyen:
        ts.in_thong_tin()
        print("-" * 30)

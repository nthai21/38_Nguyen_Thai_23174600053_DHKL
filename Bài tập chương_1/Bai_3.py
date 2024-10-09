class PS:
    def __init__(self, tu=0, mau=1):
        self.tu = tu
        self.mau = mau
        self.kiem_tra_tinh_hop_le()

    def kiem_tra_tinh_hop_le(self):
        if self.mau == 0:
            raise ValueError("Mẫu số không được bằng 0!")

    def nhap_phan_so(self):
        self.tu = int(input("Nhập tử số: "))
        self.mau = int(input("Nhập mẫu số: "))
        self.kiem_tra_tinh_hop_le()

    def in_phan_so(self):
        print(f"Phân số: {self.tu}/{self.mau}")


# Chương trình chính
if __name__ == "__main__":
    try:
        phan_so = PS()
        phan_so.nhap_phan_so()
        phan_so.in_phan_so()
    except ValueError as e:
        print(e)


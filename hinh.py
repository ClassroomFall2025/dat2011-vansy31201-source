class HinhChuNhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def tinh_chu_vi(self):
        return (self.dai + self.rong) * 2
    
    def tinh_dien_tich(self):
        return self.dai * self.rong
    
class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)
        self.canh = canh

    def xuat_thong_tin(self):
        print("Hình vuông")
        print(f"Cạnh: {self.canh}")
        print(f"Hình chữ nhật: {self.tinh_chu_vi}, Diện tích: {self.tinh_dien_tich}")
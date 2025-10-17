class SinhVienPoLy:
    # khởi tạo các thuộc tính
    def __init__(self, ho_ten, nganh_hoc):
        self.__ho_ten = ho_ten
        self.__nganh_hoc = nganh_hoc

    # tinh điểm
    def get_diem(self): # Tạo get_diem để so sánh trong get_hoc_luc
        pass

    # xếp học lực
    def get_hoc_luc(self):
        if self.get_diem() >= 9 and self.get_diem() <= 10:
            hoc_luc = "Xuất sắc"
        elif self.get_diem() >= 8:
            hoc_luc = "Giỏi"
        elif self.get_diem() >= 7:
            hoc_luc = "Khá"
        elif self.get_diem() >= 5:
            hoc_luc = "Trung bình"
        elif self.get_diem() >= 0:
            hoc_luc = "Chưa đạt"
        else:
            print("Điểm không hợp lệ")
        return hoc_luc
    
    # xuát thông tin
    def __str__(self):
        return f"họ và tên: {self.__ho_ten}, ngành: {self.__nganh_hoc}, học lực: {self.get_diem()}, {self.get_hoc_luc()}"

    # hàm xuất thông tin
    # def xuat(self):
    #     print(f"họ và tên: {self.__ho_ten}, ngành: {self.__nganh_hoc}, học lực: {self.get_diem()}, {self.get_hoc_luc()}")

    def xuat(self):
        print(f"{self.__ho_ten:^20}|{self.__nganh_hoc:^15}|{self.get_diem():^6.1f}|{self.get_hoc_luc():^15}")
    
class SinhVienIT(SinhVienPoLy):
        def __init__(self, ho_ten, nganh_hoc, diem_html, diem_java, diem_css):
            super().__init__(ho_ten, nganh_hoc) # thừa kế lớp cha
            self.__diem_html = diem_html
            self.__diem_java = diem_java
            self.__diem_css = diem_css

        def get_diem(self):
            return (self.__diem_java * 2 + self.__diem_html + self.__diem_css) / 4
        
        
class SinhVienBiz(SinhVienPoLy):
    def __init__(self, ho_ten, nganh_hoc, diem_marketting, diem_sales):
        super().__init__(ho_ten, nganh_hoc)
        self.__diem_marketting = diem_marketting
        self.__diem_sales = diem_sales

    def get_diem(self):
        return (self.__diem_marketting * 2 + self.__diem_sales) / 3
    
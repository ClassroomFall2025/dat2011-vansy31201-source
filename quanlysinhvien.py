import sinhvienpoly as svpl

class QuanLySinhVien:
    # khởi tạo một danh sách sinh viên ban đầu rỗng
    def __init__(self):
        self.dssv = []

    # phương thức nhập sinh viên:
    def nhap_danh_sach_sinh_vien(self):
        while True:
            ho_ten = input("Nhập họ tên sinh viên: ")
            nganh_hoc = input("Nhập ngành học: ")
            if nganh_hoc.lower() == "IT":
                diem_html = float("Nhập điểm html: ")
                diem_java = float("Nhập điểm java: ")
                diem_css = float("Nhập điểm css: ")
                sv = svpl.SinhVienIT(ho_ten, nganh_hoc,diem_html, diem_java, diem_css)
                self.dssv.append(sv)
            elif nganh_hoc.lower() == "Biz":
                diem_marketing = float(input("Nhập điểm marketing: "))
                diem_sales = float(input("Nhập điểm sales: "))
                sv = svpl.SinhVienBiz(ho_ten, nganh_hoc, diem_marketing, diem_sales)
            elif nganh_hoc.lower() == "Quiz":
                break
            else:
                print("Nhập không hợp lệ.")
        return self.dssv
    # phương thức xuất danh sách sinh viên
    def xuat_danh_sach_sinh_vien(self):
        if not self.dssv:
            print("Danh sách sinh viên trống.")
        else:
            print(f"Tên: {"Tên sinh viên"}, {"ngành học"}, {"điểm"}, {"học lực"}")
            for sv in self.dssv:
                sv.xuat()
    # phương thức xuất dssv giỏi    
    def xuat_dssv_gioi(self):
        pass
    
    # phương thức sap_xep_dssv
    def sap_xep_dssv(self):
        pass
import sinhvienpoly as svpl

class QuanLySinhVien:
    # khởi tạo một danh sách sinh viên ban đầu rỗng
    def __init__(self):
        self.dssv = []

    # phương thức nhập sinh viên:
    def nhap_danh_sach_sinh_vien(self):
        while True:
            ho_ten = input("Nhập họ tên sinh viên: ")
            if ho_ten.lower() == "q":
                break

            nganh_hoc = input("Nhập ngành học: ")
            if nganh_hoc.lower() == "it":
                diem_html = float(input("Nhập điểm html: "))
                diem_java = float(input("Nhập điểm java: "))
                diem_css = float(input("Nhập điểm css: "))
                sv = svpl.SinhVienIT(ho_ten, nganh_hoc,diem_html, diem_java, diem_css)
                self.dssv.append(sv)

            elif nganh_hoc.lower() == "biz":
                diem_marketing = float(input("Nhập điểm marketing: "))
                diem_sales = float(input("Nhập điểm sales: "))
                sv = svpl.SinhVienBiz(ho_ten, nganh_hoc, diem_marketing, diem_sales)
                self.dssv.append(sv)

            else:
                print("Nhập không hợp lệ.")
        return self.dssv
    # phương thức xuất danh sách sinh viên

    def xuat_danh_sach_sinh_vien(self):
        if not self.dssv:
            print("Danh sách sinh viên trống.")
        else:
            print(f"{'Tên Nhân Viên':^20}|{'Ngành học':^15}|{'Điểm':^6}|{'Học lực':^15}")
            for sv in self.dssv:
                sv.xuat()

    # phương thức xuất dssv giỏi    
    def xuat_dssv_gioi(self):
        for sv_gioi in self.dssv:
            if sv_gioi.get_hoc_luc() == "Giỏi" or sv_gioi.get_hoc_luc() == "Xuất sắc":
                sv_gioi.xuat()
    
    # phương thức sap_xep_dssv
    def sap_xep_dssv(self):
        self.dssv = sorted(self.dssv, key=lambda sv:sv.get_diem(), reverse=True)
        for sv in self.dssv:
            sv.xuat()
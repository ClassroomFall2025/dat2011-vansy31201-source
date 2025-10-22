# XÂY DỰNG HÀM BÀI ASSIGNMENT GIAI ĐOẠN I
import nhanvien as nv
class QuanLyNhanVien:
    def __init__ (self):
        self.ds_nhan_vien = []
        self.ds_HC = []
        self.ds_TT = []
        self.ds_TP = []

    def nhap_ds_nv(self):
        while True:
            ho_ten = input("\nNhập họ tên nhân viên: ")
            if ho_ten.upper() == "E":
                break
            loai_nv = input("Nhập loại nhân viên (HC, TT, TP): ")
            if loai_nv.upper() == "HC":
                while True:
                    try:
                        ma_nv = int(input("Nhập mã nhân viên: "))
                        break
                    except ValueError:
                        print("Nhập sai")
                while True:
                    try:
                        thu_nhap = int(input("Nhập thu nhập: "))
                        break
                    except ValueError:
                        print("Nhập sai")
                hc = nv.NhanVienHanhChinh(ho_ten, ma_nv, thu_nhap)
                self.ds_HC.append(hc)
                self.ds_nhan_vien.append(hc)

            elif loai_nv.upper() == "TT":
                while True:
                    try:
                        ma_nv = int(input("Nhập mã nhân viên: "))
                        break
                    except ValueError:
                        print("Nhập sai")
                while True:
                    try:
                        thu_nhap = int(input("Nhập thu nhập: "))
                        break
                    except ValueError:
                        print("Nhập sai")
                while True:
                    try:
                        doanh_so = int(input("Nhập doanh số: "))
                        break
                    except ValueError:
                        print("Nhập sai.")
                while True:
                    try:
                        ti_le_hoa_hong = float(input("Nhập tỉ lệ hoa hồng: "))/100
                        break
                    except ValueError:
                        print("Nhập sai.")
                tt = nv.TiepThi(ho_ten,ma_nv,thu_nhap,doanh_so,ti_le_hoa_hong)
                self.ds_TT.append(tt)
                self.ds_nhan_vien.append(tt)
            
            elif loai_nv.upper() == "TP":
                while True:
                    try:
                        ma_nv = int(input("Nhập mã nhân viên: "))
                        break
                    except ValueError:
                        print("Nhập sai.")
                while True:
                    try:
                        thu_nhap = int(input("Nhập thu nhập: "))
                        break
                    except ValueError:
                        print("Nhập sai.")
                while True:
                    try:
                        trach_nhiem = int(input("Nhập lương trách nhiệm: "))
                        break
                    except ValueError:
                        print("Nhập sai.")
                tp = nv.TruongPhong(ho_ten, ma_nv, thu_nhap,trach_nhiem)
                self.ds_TP.append(tp)
                self.ds_nhan_vien.append(tp)

            elif loai_nv.upper() == "E":
                break

            else:
                print("Không có bậc nhân viên này! Vui lòng nhập lại (E để nhập lại tên)")
        return self.ds_nhan_vien
    
    
    
    def xuat_ds_theo_loai(self):
        if not self.ds_HC:
            print("Danh sách nhân viên hành chính trống!")
        else:
            print("\nLoại nhân viên: hành chính")
            print("="*55)
            print(f"{"Họ và tên":^20} | {"Mã NV":^10} | {"Thu nhập":^15}")
            print("-"*55)
            for nv_hc in self.ds_HC:
                nv_hc.xuat_thong_tin()
            print("="*55)

        if not self.ds_TT:
            print("Danh sách nhân viên tiếp thị trống!")
        else:
            print("\nLoại nhân viên: tiếp thị")
            print("="*90)
            print(f"{"Họ và tên":^15} | {"Mã NV":^10} | {"Thu nhập":^15} | {"Doanh số":^15} | {"Tỉ lệ hoa hồng":^15}")
            print("-"*90)
            for nv_tt in self.ds_TT:
                nv_tt.xuat_thong_tin()
            print("="*90)

        if not self.ds_TP:
            print("\nDanh sách nhân viên trưởng phòng trống!")
        else:
            print("\nLoại nhân viên: trưởng phòng")
            print("="*73)
            print(f"{"Họ và tên":^15} | {"Mã NV":^10} | {"Thu nhập":^15} | {"Lương trách nhiệm":^10}")
            print("-"*73)
            for nv_tp in self.ds_TP:
                nv_tp.xuat_thong_tin()
            print("="*73)
        
    def luu_file(self):
        with open("Danhsach.txt", "w", encoding="utf-8") as f:
            f.write("=" * 7 + "DANH SÁCH NHÂN VIÊN HÀNH CHÍNH" + "=" * 7)
            f.write(f"\n{"Họ và tên":^15} | {"Mã nhân viên":^15} | {"Thu nhập":^15}\n")
            for nv in self.ds_HC:
                f.write(f"{nv.ho_ten:^15} | {nv.get_ma_nv():^15} | {nv.get_thu_nhap():^15}\n")

            f.write("\n")
            f.write("====" * 7 + "DANH SÁCH NHÂN VIÊN TIẾP THỊ" + "====" * 7)
            f.write(f"\n{"Họ và tên":^15} | {"Mã nhân viên":^17} | {"Thu nhập":^15} | {"Doanh số":^10} | {"Tỉ lệ hoa hồng":^15}\n")
            for nv in self.ds_TT:
                f.write(f"{nv.ho_ten:^15} | {nv.get_ma_nv():^17} | {nv.get_thu_nhap():^15} | {nv.doanh_so:^10} | {nv.ti_le_hoa_hong:^15}\n")

            f.write("\n")
            f.write("===" * 6 + "DANH SÁCH NHÂN VIÊN TRƯỞNG PHÒNG" + "===" * 6)
            f.write(f"\n{"Họ và tên":^15} | {"Mã nhân viên":^10} | {"Thu nhập":^15} | {"Lương trách nhiệm":^10}\n")
            for nv in self.ds_TP:
                f.write(f"{nv.ho_ten:^15} | {nv.get_ma_nv():^12} | {nv.get_thu_nhap():^15} | {nv.trach_nhiem:^10}\n")

    def tim_nv_theo_luong (self):
        tim_luong = []
        min_luong = int(input("Nhập lương thấp nhất: "))
        max_luong = int(input("Nhập lương cao nhất: "))
        for nv in self.ds_nhan_vien:
            if min_luong <= nv.tinh_thu_nhap() <= max_luong:
                tim_luong.append(nv)
            else:
                print("Không có nhân viên trong khoảng lương này.")
        
        for luong in tim_luong:
            luong.xuat_tt()
    
    def doc_tu_file(self):
        with open("Danhsach.txt", "r", encoding="utf-8") as f:
            for line in f:
                print(line)

    def tim_nv_theo_ma(self):
        tim_ma = []
        ma = int(input("Nhập mã cần tìm: "))
        for nv in self.ds_nhan_vien:
            if nv.get_ma_nv() == ma:
                tim_ma.append(nv)
        for i in tim_ma:
            i.xuat_tt()  # cái này không biết cách xuất theo loại nào, những làm hàm xuất thông tin cơ bản

                 
    def xoa_nv_theo_ma(self):
        xoa_ma = int(input("Nhập mã cần xóa: "))
        for nv in self.ds_nhan_vien:
            if nv.get_ma_nv() == xoa_ma:
                self.ds_nhan_vien.remove(nv)
                print("Đã xóa nhân viên có mã: ", xoa_ma)
                return    # nó đã xóa nhân viên có mã đó, khi tìm nv theo ma sẽ không thấy nv đó nữa

    def sap_xep_nv_theo_thu_nhap(self):
        self.ds_nhan_vien = sorted(self.ds_nhan_vien, key=lambda nv:nv.get_thu_nhap(), reverse=True)
        for i in self.ds_nhan_vien:
            i.xuat_tt()

    def sap_xep_nv_theo_ho_ten(self):
        self.ds_nhan_vien = sorted(self.ds_nhan_vien, key=lambda nv:nv.ho_ten, reverse=True)
        for i in self.ds_nhan_vien:
            i.xuat_tt()
    
    def xuat_5_nv_thu_nhap_cao_nhat(self):
        self.ds_nhan_vien = sorted(self.ds_nhan_vien, key=lambda nv:nv.get_thu_nhap(), reverse=True)
        for i in self.ds_nhan_vien[:5]:
            i.xuat_tt()

    def cap_nhat_tt_theo_ma(self):
        ma_nv = int(input("Nhập mã nhân viên muốn sửa: "))
        for nv in self.ds_nhan_vien:
            if nv.get_ma_nv() == ma_nv:
                ten_moi = input("Nhập tên mới: ")
                nv.ho_ten = ten_moi

                ma_moi = int(input("Nhập mã mới: "))
                nv.set_ma_nv(ma_moi)

                thu_nhap_moi = int(input("Nhập thu nhập mới: "))
                nv.set_thu_nhap(thu_nhap_moi)
                
                print("Cập nhật thông tin thành công!")
                break # chỉ cập nhật được họ tên vào danh sách nhưng không thể cập nhập mã và thu nhập

    
            
    




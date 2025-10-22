class NhanVienHanhChinh:
    def __init__(self, ho_ten, ma_nv, thu_nhap):
        self.ho_ten = ho_ten
        self.__ma_nv = ma_nv
        self.__thu_nhap = thu_nhap
    
    def get_ma_nv(self):
        return self.__ma_nv
    
    def set_ma_nv(self, ma_nv):
        self.__ma_nv = ma_nv
    
    def get_thu_nhap(self):
        return self.__thu_nhap
    
    def set_thu_nhap(self, thu_nhap):
        self.__thu_nhap = thu_nhap

    def tinh_thu_nhap(self):
        return self.__thu_nhap

    def thue_thu_nhap(self):
        if self.get_thu_nhap() < 9000000:
            return 0
        elif self.get_thu_nhap() < 15000000:
            return (self.tinh_thu_nhap()-9000000) * 0.1
        else:
            return (self.tinh_thu_nhap()-15000000) *1.2

    def thu_nhap_sau_thue(self):
        return self.tinh_thu_nhap() - self.thue_thu_nhap()
    
    def xuat_thong_tin(self):
        print(f"{self.ho_ten:^20} | {self.get_ma_nv():^10} | {self.get_thu_nhap():^15}")

    def xuat_tt(self):
        print("="*55)
        # print(f"{"Họ và tên":^20} | {"Mã NV":^10} | {"Thu nhập":^15}")
        print(f"{self.ho_ten:^20} | {self.get_ma_nv():^10} | {self.get_thu_nhap():^15}")
        print("-"*55)
        

class TiepThi(NhanVienHanhChinh):
    def __init__(self,ho_ten, ma_nv, thu_nhap, doanh_so, ti_le_hoa_hong):
        super().__init__(ho_ten, ma_nv, thu_nhap)
        self.doanh_so = doanh_so
        self.ti_le_hoa_hong = ti_le_hoa_hong
    
    def nhap_thong_tin(self):
        super().nhap_thong_tin()
        self.doanh_so = int(input("Nhập doanh số"))
        self.ti_le_hoa_hong = float(input("Nhập tỉ lệ hoa hồng (%): "))/100

    def xuat_thong_tin(self):
        print(f"{self.ho_ten:^15} | {self.get_ma_nv():^10} | {self.get_thu_nhap():^15} | {self.doanh_so:^15} | {self.ti_le_hoa_hong:^15}")

    def tinh_thu_nhap(self):
        return self.doanh_so*self.ti_le_hoa_hong + self.get_thu_nhap()
    
class TruongPhong(NhanVienHanhChinh):
    def __init__(self, ho_ten, ma_nv, thu_nhap, trach_nhiem):
        super().__init__(ho_ten, ma_nv, thu_nhap)
        self.trach_nhiem = trach_nhiem
    
    def nhap_thong_tin(self,):
        super().nhap_thong_tin()
        self.trach_nhiem = input("Nhập lương trách nhiệm: ")

    def xuat_thong_tin(self):
        print(f"{self.ho_ten:^15} | {self.get_ma_nv():^10} | {self.get_thu_nhap():^15} | {self.trach_nhiem:^10}")

    def tinh_thu_nhap(self):
        return self.get_thu_nhap() + self.trach_nhiem

    
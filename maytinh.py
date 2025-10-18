import math as m
import time as t
class MayTinh:
    def __init__(self, chuc_nang, lich_su_phep_tinh):
        self.chuc_nang = chuc_nang
        self.lich_su_phep_tinh = []

    def nhap_1_hs(self):
        self.hs_a = float(input("Nhập hệ số a: "))

    def nhap_2_hs(self):
        self.hs_a = float(input("Nhập hệ số a: "))
        self.hs_b = float(input("Nhập hệ số b: "))

    def nhap_3_hs(self):
        self.hs_a = float(input("Nhập hệ số a: "))
        self.hs_b = float(input("Nhập hệ số b: "))
        self.hs_c = float(input("Nhập hệ số c: "))

    def phep_tinh_co_ban(self):
        self.chuc_nang = input("Nhập chức năng phép tính: +, -, *,/")
        if self.chuc_nang == "+":
            ket_qua = self.hs_a + self.hs_b
            self.lich_su_phep_tinh.append(f"{self.hs_a} + {self.hs_b} = {ket_qua}")
            return f"{self.hs_a} + {self.hs_b} = {ket_qua}"
            
        elif self.chuc_nang == "-":
            ket_qua = self.hs_a - self.hs_b
            self.lich_su_phep_tinh.append(f"{self.hs_a} - {self.hs_b} = {ket_qua}")
            return f"{self.hs_a} - {self.hs_b} = {ket_qua}"
            
        
        elif self.chuc_nang == "*":
            ket_qua = self.hs_a * self.hs_b
            self.lich_su_phep_tinh.append(f"{self.hs_a} * {self.hs_b} = {ket_qua}")
            return f"{self.hs_a} * {self.hs_b} = {ket_qua}"
        
        elif self.chuc_nang == "/":
            if self.hs_b == 0:
                print("Không thể chia được cho 0")
            else: 
                ket_qua = self.hs_a / self.hs_b
            self.lich_su_phep_tinh.append(f"{self.hs_a} / {self.hs_b} = {ket_qua}")
            return f"{self.hs_a} / {self.hs_b} = {ket_qua}"
        
        else:
            print("Chức năng không tồn tại!")
    
    def luy_thua(self):
        ket_qua = self.hs_a ** self.hs_b
        return f"{self.hs_a}^{self.hs_b} = {ket_qua}"
    
    def can(self):
        if self.hs_a < 0:
            return 
        else:
            return f"Căn bậc hai của {self.hs_a} = {m.sqrt(self.hs_a)}"
    
    def ham_luong_giac(self):
        self.chuc_nang = input("Nhập chức năng: Sin, Cos, Tan")

        if self.chuc_nang.lower() == "sin":
            ket_qua = m.sin(self.hs_a)
            return f"Sin của {self.hs_a} = {ket_qua}"
        
        elif self.chuc_nang.lower() == "cos":
            ket_qua = m.cos(self.hs_a)
            return f"Cos của {self.hs_a} = {ket_qua}"
        
        elif self.chuc_nang.lower() == "tan":
            ket_qua = m.tan(self.hs_a)
            return f"Tan của {self.hs_a} = {ket_qua}"
        
        else:
            print("Chức năng không tồn tại!")

    def logarit(self):
        self.chuc_nang = input("Nhập chức năng: Log cơ số 10, ln, Log cơ số tùy chọn.")

        if self.chuc_nang.lower() == "log10":
            ket_qua = m.log10(self.hs_a)
            return f"Log cơ số 10 của {self.hs_a} = {ket_qua}"
        
        elif self.chuc_nang.lower() == "ln":
            co_so = float(input("Nhập cơ số log: "))
            ket_qua = m.log(self.hs_a, co_so)
            return f"Log({self.hs_a, co_so}) = {ket_qua}"
        
        elif self.chuc_nang.lower() == "log":
            ket_qua = m.log(self.hs_a)
            return f"Log({self.hs_a}) = {ket_qua}"
        
        else:
            print("Chức năng không tồn tại!")

    def phuong_trinh_bac_nhat(self):
        if self.hs_a == 0:
            if self.hs_b == 0:
                return "Phương trình vô số nghiệm"
            else:
                return "Phương trình vô nghiệm"
        else:
            ket_qua = -self.hs_b / self.hs_a
            return f"Nghiệm X = {ket_qua}"
    
    def phuong_trinh_bac_hai(self):
        if self.hs_a == 0:
            if self.hs_b == 0:
                if self.hs_c == 0:
                    return "Phương trình vô số nghiệm"
                else:
                    return "Phương trình vô nghiệm"
            else:
                ket_qua = -self.hs_c / self.hs_b
                return f"Phương trình bậc nhất X = {ket_qua}"
        else:
            delta = self.hs_b * self.hs_b - 4 * self.hs_a * self.hs_c
            if delta > 0:
                x1 = (-self.hs_b + m.sqrt(delta))/ (2*self.hs_a)
                x2 = (-self.hs_b - m.sqrt(delta))/ (2*self.hs_a)
                return f"Phương trình có 2 nghiệm phân biệt x1 = {x1}, x2 = {x2}"
            elif delta == 0:
                ket_qua = -self.hs_b / (2*self.hs_a)
                return f"Phương trình có nghiệm kép X1 = X2 = {ket_qua}"
            else:
                return "Phương trình vô nghiệm"
            
    def lich_su(self):
        if len(self.lich_su_phep_tinh) == 0:
            print("Lịch sử trống.")
        else:
            for k,v in enumerate(self.lich_su_phep_tinh, start=1):
                return f"{k}: {v}"
            
    def thoi_gian(self):
        return t.datetime.now().strftime("%d/%M/%Y %H:%M:%S")
            

            

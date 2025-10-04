import math
import datetime
# TÍNH TIỀN NƯỚC
def tinh_tien_nuoc(so_nuoc):
    gia_ban_nuoc = (7500, 8800, 12000, 24000)
    if so_nuoc <= 10:
        tien_nuoc =  so_nuoc * gia_ban_nuoc[0]
    elif so_nuoc <= 20:
        tien_nuoc = 10 * gia_ban_nuoc[0] + (so_nuoc - 10) * gia_ban_nuoc[1]
    elif so_nuoc <= 30:
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + (so_nuoc - 20) * gia_ban_nuoc[2]
    else:
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] + (so_nuoc - 30) * gia_ban_nuoc[3]
    return tien_nuoc

# TÍNH NGUYÊN LIỆU LÀM BÁNH
def tinh_nguyen_lieu(sl_bdx, sl_btc, sl_bd):
    banh_dau_xanh = {"Đường": 0.04, "Đậu": 0.07}
    banh_thap_cam = {"Đường": 0.06, "Đậu": 0}
    banh_deo = {"Đường": 0.05, "Đậu": 0.02}
    nguyen_lieu = {}
    duong_hop_banh = sl_bdx * banh_dau_xanh["Đường"] + sl_btc * banh_thap_cam["Đường"] + sl_bd * banh_deo["Đường"]
    dau_hop_banh = sl_bdx * banh_dau_xanh["Đậu"] + sl_btc * banh_thap_cam["Đậu"] + sl_bd * banh_deo["Đậu"]
    nguyen_lieu["Đường"] = duong_hop_banh
    nguyen_lieu["Đậu"] = dau_hop_banh
    return nguyen_lieu

# BÀI LÀM THÊM VIẾT HÀM CÁC PHÉP TÍNH:
def tong(a, b):
    ket_qua = a + b
    return ket_qua

def hieu(a, b):
    ket_qua = a - b
    return ket_qua

def tich(a, b):
    ket_qua = a * b
    return ket_qua

def thuong(a, b):
    if b == 0:
        return
    ket_qua = a/b
    return ket_qua

def luy_thua(a, b):
    ket_qua = a ** b
    return ket_qua

def can_bac2(a):
    if a < 0:
        return
    ket_qua = math.sqrt(a)
    return ket_qua

def sin(a):
    ket_qua = math.sin(a)
    return ket_qua

def cos(a):
    ket_qua = math.cos(a)
    return ket_qua

def tan(a):
    ket_qua = math.tan(a)
    return ket_qua

def log10(a):
    ket_qua = math.log10(a)
    return ket_qua

def ln(a, b):
    ket_qua = math.log(a, b)
    return ket_qua

def log(a):
    ket_qua = math.log(a)
    return ket_qua

def pt_1(a, b):
    if a == 0:
        if b == 0:
            return "Phương trình vô số nghiệm"
        else:
            return "Phương trình vô nghiệm"
    else:
        return -b/a

def pt_2(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Phương trình vô số nghiệm" 
            else:
                return "Phương trình vô nghiệm"
        else:
            return -c/b
    else:     
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            return f"Phương trình có hai nghiệm phân biệt x1 = {x1}, x2 = {x2}"
        elif delta == 0:
            x = -b / (2*a)
            return f"Phương trình có nghiệm kép: x1 = x2 = {x}"
        else:
            return "Phương trình vô nghiệm"

def xem_lich_su(lich_su):
    if len(lich_su) == 0:
        return "Lịch sử trống, chưa có chức năng nào được chọn"
    else:
        return "======Lịch sử======\n"
        for i, j in enumerate(lich_su, start = 1):
            return f"{i}. {j}\n"

def thoi_gian():
    return datetime.datetime.now().strftime("%d/%M/%Y %H:%M:%S")
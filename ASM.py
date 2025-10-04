# XÂY DỰNG HÀM BÀI ASSIGNMENT GIAI ĐOẠN I
def nhap_ds_nv():
    pass
def luu_file():
    pass

def doc_tu_file():
    pass

def xuat_ds():
    pass

def tim_nv_theo_luong ():
    pass

def tim_nv_theo_ma():
    pass

def tim_kiem_nhan_vien():
    pass
                 
def xoa_nv_theo_ma():
    pass

def sap_xep_nv_theo_thu_nhap():
    pass

def sap_xep_nv_theo_ho_ten():
    pass

def sap_xep_nv_():
    print("*"*15+" SẮP XẾP NHÂN VIÊN "+"*"*16)
    print("|    1. Sắp xếp nhân viên theo tên               |")
    print("|    2. Sắp xếp nhân viên theo thu nhập          |")
    print("*"*50)
    print("Chọn phương thức tìm kiếm")
    while True:
        try:
            sap_xep = int(input("Bạn hãy chon 1 hoặc 2: "))
            if sap_xep in [1,2]:
                break
        except ValueError:
            print("Lựa chọn không hợp lệ ! Vui lòng nhập lại lựa chọn.")
    if sap_xep == 1:
        list_tim_kiem=sap_xep_nv_theo_ho_ten()
    elif sap_xep == 2:
        list_tim_kiem=sap_xep_nv_theo_thu_nhap()
    else:
        print("Thoát sắp xếp")
    return 

def cap_nhat_tt_theo_ma():
    pass

def xuat_5_nv_thu_nhap_cao_nhat():
    pass




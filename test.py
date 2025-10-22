from ASM import *
from nhanvien import *

nhan_vien = QuanLyNhanVien()

menu_list = {
    0: "Thoát chương trình",
    1: "Nhập danh sách nhân viên từ bàn phím và lưu vào file",
    2: "Đọc thông tin nhân viên từ file và xuất danh sách",
    3: "Tìm và hiển thị nhân viên theo mã nhập từ bàn phím.",
    4: "Xóa nhân viên theo mã nhập từ bàn phím. Cập nhật file dữ liệu",
    5: "Cập nhật thông tin nhân viên theo mã nhập từ bàn phím và ghi thay đổi vào file",
    6: "Tìm các nhân viên theo khoảng lương nhập từ bàn phím",
    7: "Sắp xếp nhân viên theo họ và tên.", 
    8: "Sắp xếp nhân viên theo thu nhập",
    9: "Xuất 5 nhân viên có thu nhập cao nhất"
}


print("="*26+"MENU CHƯƠNG TRÌNH"+"="*25)
for key, value in menu_list.items():
    print(f" {key} : {value} {(55 - len(value)) * ' '}")
print("="*64)

while True:
    while True:
        try:
            lua_chon = int(input("Nhập lựa chọn của bạn từ 0 - 7: "))
            break
        except ValueError:
            print("Lựa chọn không hợp lệ,vui lòng nhập lại lựa chọn")
    match lua_chon:
        case 0:
            break
        case 1:
            nhan_vien.nhap_ds_nv()
            nhan_vien.luu_file()
        case 2:
            nhan_vien.doc_tu_file()
            nhan_vien.xuat_ds_theo_loai()
        case 3:
            nhan_vien.tim_nv_theo_ma()
        case 4:
            nhan_vien.xoa_nv_theo_ma()
        case 5:
            nhan_vien.cap_nhat_tt_theo_ma()
        case 6:
            nhan_vien.sap_xep_nv_theo_thu_nhap()
        case 7:
            nhan_vien.sap_xep_nv_theo_ho_ten()
        case 8:
            nhan_vien.tim_nv_theo_luong()
        case 9:
            nhan_vien.xuat_5_nv_thu_nhap_cao_nhat()
        case _:
            print("Lựa chọn không hợp lệ.")
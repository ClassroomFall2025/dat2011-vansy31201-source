import math as m
class SanPham:
    def __init__(self, ten="", gia=0, giam_gia=0):
        self.__ten = ten
        self.__gia = gia
        self.__giam_gia = giam_gia

    
    def get_ten_sp(self):
        return self.__ten
    
    def set_ten_sp(self, ten):
        self.__ten = ten

    def get_gia(self):
        return self.__gia
    
    def set_gia(self, gia):
        self.__gia = gia


    def get_giam_gia(self):
        return self.__giam_gia
    
    def set_giam_gia(self, giam_gia):
        self.__giam_gia = giam_gia

    def thue(self):
        return self.__gia * 0.1
    
    def xuat_tt(self):
        print(f'Sản phẩm {self.__ten}, giá {self.__gia}, giá giảm {self.__giam_gia}, thuế {self.thue()}')
    
    def nhap_sp(self):
        self.__ten = input('Tên sản phẩm: ')
        self.__gia = float(input('Giá sản phẩm: '))
        self.__giam_gia = float(input('Giảm giá: '))



    

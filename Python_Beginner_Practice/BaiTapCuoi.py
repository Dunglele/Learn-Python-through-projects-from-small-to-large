class Book:
    def __init__(self, tieu_de, tac_gia):
        self._tieu_de = tieu_de
        self._tac_gia = tac_gia
        self._gia_ban = 0

    @property
    def tieu_de(self):
        return self._tieu_de
    @property
    def tac_gia(self):
        return self._tac_gia
    @property
    def gia_ban(self):
        return self._gia_ban
    @gia_ban.setter
    def gia_ban(self, value):
        if(value <= 0):
            print("\nGia ban phai lon hon 0")
        else:
            self._gia_ban = int(value)

    def tinh_gia_cuoi_cung(self):
        pass
    def __str__(self):
        pass

class PhysicalBook(Book):
    def __init__(self, tizeu_de, tac_gia, can_nang):
        super().__init__(tieu_de, tac_gia)
        self.can_nang = can_nang
    
    def tinh_gia_cuoi_cung(self):
        super().tinh_gia_cuoi_cung()
        gia = self._gia_ban + (self.can_nang * 2000)
        return gia

    def __str__(self):
        super().__str__()
        return(f"[PhysicalBook] {self._tieu_de} - " + str(self._gia_ban) + "d")
    
class Ebook(Book):
    def __init__(self, tieu_de, tac_gia, dung_luong, dinh_dang):
        super().__init__(tieu_de, tac_gia)
        self.dung_luong = dung_luong
        self.dinh_dang = dinh_dang
    def tinh_gia_cuoi_cung(self):
        super().tinh_gia_cuoi_cung()
        return self._gia_ban
    def __str__(self):
        super().__str__()
        return(f"[EBOOK] {self._tieu_de} - " + str(self._gia_ban) + "d")

def main():
    print("\n-----")
    name = input("\nNhap ten sach: ")
    author = input("Nhap ten tac gia: ")
    price = int(input("Nhap gia tien: "))
    capacity = input("Nhap dung luong (MB): ")
    format = input("Nhap dinh dang: ")
    loaiSach = "Ebook"
    eBook = Ebook(name, author, capacity, format)
    eBook.gia_ban = price
    eBook.__str__()
    print("\nGia cuoi cung: " + str(eBook.tinh_gia_cuoi_cung()))

if __name__ == "__main__":
    main()
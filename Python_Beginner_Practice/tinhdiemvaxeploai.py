class SinhVien():
    def __init__(self, id, name, math, literature, english):

        self.id = id
        self.name = name
        self.math = math
        self.literature = literature
        self.english = english
        self.newTB = (self.math + self.literature + self.english) / 3

        if(self.newTB >= 8):
            self.rank = "Gioi"
        if(self.newTB >= 7 and self.newTB < 8):
            self.rank = "Kha"
        if(self.newTB >= 5 and self.newTB < 7):
            self.rank = "Trung binh"
        if(self.newTB < 5):
            self.rank = "Yeu"

    def show_sv(self):

        print(f"\nID: {self.id}, Name: {self.name}")
    
    def show_full(self):

        print(f"\nID: {self.id}, Name: {self.name}")
        print(f"\nDiemTB: {self.newTB}, Xep Loai: {self.rank}")

class QuanLyLopHoc():
    def __init__(self):

        self.listSV = []
    
    def them_sinh_vien(self):
        
        self.newID = int(input("\nNhap ID moi: "))
        self.newName = input("Nhap ten sinh vien: ")
        self.newMath = float(input("Nhap diem mon toan: "))
        self.newLiterature = float(input("Nhap diem mon van: "))
        self.newEnglish = float(input("Nhap diem mon anh: "))
        
        self.newSV = SinhVien(self.newID, self.newName, self.newMath, self.newLiterature, self.newEnglish)

        self.listSV.append(self.newSV)

        print("\nThem sinh vien voi ID: " + str(self.newID) + " thanh cong !!!")

    def danh_sach_sinh_vien(self):
        print("\n")
        print("-----")
        print("\nDanh sach sinh vien")
        for i in self.listSV:
            i.show_sv()

    def tim_sinh_vien_gioi(self):
        print("\n")
        print("-----")
        print("\nTim sinh vien gioi")
        for i in self.listSV:
            if(i.rank == "Gioi"):
                i.show_full()

    def hien_thi_day_du(self):
        print("\n")
        print("-----")
        print("\nDanh sach sinh vien day du")
        for i in self.listSV:
            i.show_full()
            
def rollback(lopHoc):
    print("\n-----")
    option = input("\nDa hoan thanh yeu cau, ban co muon tiep tuc su dung (y/n): ")
    if(option == "y"):
        return switch_case(lopHoc)
    return 0

def switch_case(lopHoc):

    print("\n")
    print("-----")
    print("\nChao mung den voi he thong quan ly diem sinh vien")
    print("\n1.Them sinh vien")
    print("\n2.Hien thi danh sach sinh vien")
    print("\n3.Tim sinh vien gioi")
    print("\n4.Hien thi danh sach sinh vien day du")
    print("\n5.Thoat")

    option = int(input("\nVui long dua ra lua chon cua ban: "))

    match option:
        case 1:
            lopHoc.them_sinh_vien()
            return rollback(lopHoc)
        case 2:
            lopHoc.danh_sach_sinh_vien()
            return rollback(lopHoc)
        case 3:
            lopHoc.tim_sinh_vien_gioi()
            return rollback(lopHoc)
        case 4:
            lopHoc.hien_thi_day_du()
            return rollback(lopHoc)
        case 5:
            return 0

def main():
    lopHoc = QuanLyLopHoc()
    switch_case(lopHoc)

if __name__ == "__main__":
    main()
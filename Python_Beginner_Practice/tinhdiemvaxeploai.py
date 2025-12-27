DanhSachSinhVien = [
    {'id': 1, 'name': 'Nguyen Hai Duong', 'math': 10.0, 'literature': 10.0, 'english': 10.0},
    {'id': 2, 'name': 'Dinh Pham Ngoc Khanh', 'math': 8.0, 'literature': 10.0, 'english': 7.0},
    {'id': 3, 'name': 'Le Xuan Khanh Duy', 'math': 7.0, 'literature': 7.0, 'english': 7.0},
    {'id': 4, 'name': 'Nguyen Le Tien Anh', 'math': 9.0, 'literature': 4.0, 'english': 6.0},
    {'id': 5, 'name': 'Nguyen Dang Khoa', 'math': 6.0, 'literature': 5.0, 'english': 6.0}

]

diemTB = []
xepLoai = []

class SinhVien():
    def __init__(self, listSV):

        self.listSV = listSV
        
    def tinh_trung_binh(self, id, math, literature, english, diemTB):

        self.diemTB = diemTB
        self.diemTrungBinh = (math + literature + english) / 3

        newDiemTB = {'id': id, 'diemTB': self.diemTrungBinh}
        self.diemTB.append(newDiemTB)

    def xep_loai(self, id, diemtb, xepLoai):

        self.xepLoai= xepLoai

        if(diemtb >= 8):
            self.rank = "Gioi"
        if(diemtb < 8 and diemtb >= 6.5):
            self.rank = "Kha"
        if(diemtb < 6.5 and diemtb >= 5):
            self.rank = "Trung binh"
        if(diemtb < 5):
            self.rank = "Yeu"

        newXepLoai = {'id': id, 'rank': self.rank}
        self.xepLoai.append(newXepLoai)

    def hien_thi_thong_tin(self, listSV, listTB, listRank):
        id = 1
        for i in listSV:
            if(i['id'] == id):
                for j in listTB:
                    if(j['id'] == i['id']):
                        for k in listRank:
                            if(k['id'] == i['id']):
                                print(f"\nID: {i['id']}, Name: {i['name']}, DTB: {j['diemTB']}, Xep Loai: {k['rank']}")
                                id += 1

class QuanLyLopHoc(SinhVien):
    def them_sinh_vien(self, listSV):

        newID = int(input("\nNhap ID moi: "))
        newName = input("Nhap ten sinh vien: ")
        newMath = float(input("Nhap diem mon toan: "))
        newLiterature = float(input("Nhap diem mon van: "))
        newEnglish = float(input("Nhap diem mon anh: "))

        newSV = {'id': newID, 'name': newName, 'math': newMath, 'literature': newLiterature, 'english': newEnglish}

        listSV.append(newSV)

        print("\nThem sinh vien voi ID: " + str(newID) + " thanh cong !!!")

    def tim_sinh_vien_gioi(self, listSV, listTB, listRank):
        for i in listRank:
            if(i['rank'] == "Gioi"):
                for j in listSV:
                    if(j['id'] == i['id']):
                        for k in listTB:
                            if(k['id'] == i['id']):
                                print(f"\nID: {i['id']}, Name: {j['name']}, DTB: {k['diemTB']}, Xep Loai: {i['rank']}")

def danh_sach_sinh_vien():
    print("\n")
    print("-----")
    print("\nDanh sach sinh vien")
    sinhVien = SinhVien(DanhSachSinhVien)
    for i in sinhVien.listSV:
        print(f"\nID: {i['id']}, Name: {i['name']}")

    return rollback()

def diem_trung_binh_chung():
    print("\n")
    print("-----")
    print("\nDiem trung binh chung")
    sinhVien = SinhVien(DanhSachSinhVien)
    for i in sinhVien.listSV:
        sinhVien.tinh_trung_binh(i['id'], i['math'], i['literature'], i['english'], diemTB)
    for i in diemTB:
        print(f"\nID: {i['id']}, DiemTB: {i['diemTB']}")

def xep_loai_chung():
    print("\n")
    print("-----")
    print("\nXep loai chung")
    sinhVien = SinhVien(DanhSachSinhVien)
    for i in diemTB:
        sinhVien.xep_loai(i['id'], i['diemTB'], xepLoai)
    for i in xepLoai:
        print(f"\nID: {i['id']}, Xep Loai: {i['rank']}")

def diem_trung_binh_xep_loai():
    sinhVien = SinhVien(DanhSachSinhVien)
    for i in sinhVien.listSV:
        sinhVien.tinh_trung_binh(i['id'], i['math'], i['literature'], i['english'], diemTB)
    for i in diemTB:
        sinhVien.xep_loai(i['id'], i['diemTB'], xepLoai)
    print("\n")
    print("-----")
    print("\nDanh sach diem trung binh & xep loai")
    sinhVien.hien_thi_thong_tin(DanhSachSinhVien, diemTB, xepLoai)
    return rollback()

def them_sinh_vien_moi():
    print("\n")
    print("-----")
    print("\nThem sinh vien moi")
    sinhVien = QuanLyLopHoc(DanhSachSinhVien)
    sinhVien.them_sinh_vien(DanhSachSinhVien)

    return rollback()

def tim_sinh_vien_gioi():
    sinhVien = SinhVien(DanhSachSinhVien)
    for i in sinhVien.listSV:
        sinhVien.tinh_trung_binh(i['id'], i['math'], i['literature'], i['english'], diemTB)
    for i in diemTB:
        sinhVien.xep_loai(i['id'], i['diemTB'], xepLoai)
    print("\n")
    print("-----")
    print("\nTim sinh vien gioi")
    sinhVien2 = QuanLyLopHoc(DanhSachSinhVien)
    sinhVien2.tim_sinh_vien_gioi(DanhSachSinhVien, diemTB, xepLoai)
    
    return rollback()

def rollback():
    print("\n-----")
    option = input("\nDa hoan thanh yeu cau, ban co muon tiep tuc su dung (y/n): ")
    if(option == "y"):
        return switch_case()
    return 0

def switch_case():

    print("\n")
    print("-----")
    print("\nChao mung den voi he thong quan ly diem sinh vien")
    print("\n1.Hien thi danh sach sinh vien")
    print("\n2.Hien thi diem trung binh chung")
    print("\n3.Hien thi xep loai chung")
    print("\n4.Hien thi danh sach diem trung binh & xep loai")
    print("\n5.Them sinh vien")
    print("\n6.Tim sinh vien gioi")

    option = int(input("\nVui long dua ra lua chon cua ban: "))

    match option:
        case 1:
            danh_sach_sinh_vien()
        case 2:
            diem_trung_binh_chung()
            return rollback()
        case 3:
            xep_loai_chung()
            return rollback()
        case 4:
            diem_trung_binh_xep_loai()
        case 5:
            them_sinh_vien_moi()
        case 6:
            tim_sinh_vien_gioi()


def main():
    return switch_case()
    
if __name__ == main():
    main()
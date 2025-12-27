DanhSachSinhVien = [
   {'id': 1, 'name': 'Nguyen Hai Duong', 'born_year': 2005, 'gpa': 4.0},
   {'id': 2, 'name': 'Nguyen Le Tien Anh', 'born_year': 2007, 'gpa': 3.0},
   {'id': 3, 'name': 'Dinh Pham Ngoc Khanh', 'born_year': 2005, 'gpa': 2.5},
   {'id': 4, 'name': 'Le Xuan Khanh Duy', 'born_year': 2005, 'gpa': 4.0},
   {'id': 5, 'name': 'Nguyen Dang Khoa', 'born_year': 2005, 'gpa': 1.0}

]

class SinhVien():
    def __init__(self, id, name, born_year, gpa):
       self.id = int(id)
       self.name = str(name)
       self.born_year = int(born_year)
       self.gpa = float(gpa)
       pass

class QuanLySinhVien(SinhVien):
   def hienThiSinhVien(self):
            print(f"\nID: {str(self.id)}, Name: {str(self.name)}, Born: {str(self.born_year)}, GPA: {str(self.gpa)}")
            pass

def DanhSachSV(DanhSachSinhVien):
        for i, data in enumerate(DanhSachSinhVien):
            duyetSV = QuanLySinhVien(data['id'], data['name'], data['born_year'], data['gpa']) 
            duyetSV.hienThiSinhVien()

def themSinhVien(DanhSachSinhVien):
        
        print("\n")
        print("Danh sach sinh vien hien tai")
        DanhSachSV(DanhSachSinhVien)

        print("\nDien cac thong tin sau de them sinh vien")
        print("\n-----")

        newID = int(input("\nID sinh vien: "))

        for i in DanhSachSinhVien:
            if(i['id'] == newID):
                print("\nTham so dau vao sai, hoac ID da ton tai. Vui long thu lai sau!!!")
                input("\nNhan enter de bat dau lai quy trinh!!!")
                return themSinhVien(DanhSachSinhVien)
            pass

        newName = input("Ho ten sinh vien: ")
        newBY = int(input("Nam sinh: "))
        newGPA = float(input("GPA: "))

        newSV = {'id': newID, 'name': newName, 'born_year': newBY, 'gpa': newGPA}
        DanhSachSinhVien.append(newSV)

        SinhVien(newID, newName, newBY, newGPA)
        
        input("\nSinh vien ID: " + str(newID) + " da duoc them thanh cong")

        return rollback()
        
def removeSV (DanhSachSinhVien):
    print("\n")
    print("-----")
    DanhSachSV(DanhSachSinhVien)
    option = int(input("\nNhap ID sinh vien can xoa: "))

    real_id = -1

    for i, data in enumerate(DanhSachSinhVien):
        if(data['id'] == option):
            real_id = i
        pass
    
    if(real_id == -1):
        print("\nID sinh vien khong ton tai, hoac tham so dau vao sai!!!")
        input("\n")
        return removeSV

    DanhSachSinhVien.remove(DanhSachSinhVien[real_id])
    print("\nDa xoa sinh vien voi ID: " + str(option) +" thanh cong")
    return rollback()

def updateSV(DanhSachSinhVien):
    print("\n")
    print("-----")
    DanhSachSV(DanhSachSinhVien)
    option = int(input("\nNhap ID sinh vien can sua: "))

    real_id = -1

    for i, data in enumerate(DanhSachSinhVien):
        if(data['id'] == option):
            real_id = i
        pass
    
    if(real_id == -1):
        print("\nID sinh vien khong ton tai, hoac tham so dau vao sai!!!")
        input("\n")
        return updateSV(DanhSachSinhVien)
    
    new_id = int(input("Nhap ID moi: "))

    for i in DanhSachSinhVien:
        if(i['id'] == new_id):
            print("\nTham so dau vao sai, hoac ID da ton tai. Vui long thu lai sau!!!")
            input("\nNhan enter de bat dau lai quy trinh!!!")
            return updateSV(DanhSachSinhVien)
        pass
    DanhSachSinhVien[real_id]['id'] = new_id
    DanhSachSinhVien[real_id]['name'] = input("Nhap ten moi: ")
    DanhSachSinhVien[real_id]['born_year'] = int(input("Nhap nam sinh moi: "))
    DanhSachSinhVien[real_id]['gpa'] = float(input("Nhap gpa moi: "))

    print("\nCap nhat thong tin moi thanh cong !!!")
    input("")
    return rollback()

def timKiemSV(DanhSachSinhVien):
    print("\n")
    print("-----")
    DanhSachSV(DanhSachSinhVien)
    option = int(input("\nNhap ID sinh vien can tim: "))

    print("\n-----")
    status = -1

    for i in DanhSachSinhVien:
        if(i['id'] == option):
            print(f"\nID: {i['id']}, Name: {i['name']}, Born: {i['born_year']}, GPA: {i['gpa']}")
            status = 1

    if(status == -1):
        print("\nTham so dau vao sai, hoac ID khong ton tai. Vui long thu lai sau!!!")
        input("\n")
        return timKiemSV(DanhSachSinhVien)
    
    return rollback()

def rollback():
   print("\n-----")
   option = input("\nBan co muon tiep tuc su dung chuong trinh (y/n): ")

   if(option == "y"):
      return switch_case()
   
   return 0

def switch_case():
   print("\n-----")
   print("\n1. Hien thi danh sach")
   print("\n2. Them sinh vien")
   print("\n3. Sua sinh vien")
   print("\n4. Xoa sinh vien")
   print("\n5. Tim kiem sinh vien")

   print("\n-----")
   option = int(input("\nVui long dua ra lua chon cua ban: "))

   match(option):
      case 1:
         DanhSachSV(DanhSachSinhVien)
         return rollback()
      case 2:
         themSinhVien(DanhSachSinhVien)
      case 3:
         updateSV(DanhSachSinhVien)
      case 4:
         removeSV(DanhSachSinhVien)
      case 5:
         timKiemSV(DanhSachSinhVien)
def main():
   print("\n")
   print("\n-----")
   print("\nChao mung den voi he thong Quan Ly Sinh Vien")
   switch_case()

if __name__ == "__main__":
   main()
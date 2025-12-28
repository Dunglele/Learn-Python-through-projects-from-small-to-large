class PhoneBook:
    def __init__(self):
        self.DanhBa = [] 
    def add_Contact(self):
        print("\n")
        print("-----")
        print("\nThem lien he")
        name = input("\nNhap ten lien he: ")
        phone = input("Nhap so dien thoai: ")
        email = input("Nhap email: ")
        newLienHe = Contact(name, phone, email, self.DanhBa)
        print("\n")
        option = input("Them lien he moi thanh cong, ban co muon xem danh sach (y/n): ")

        if(option == "y"):
            newLienHe.show_Contact()
        
        
    def search_Contact(self):
        print("\n")
        print("-----")
        print("\nTim lien he")
        value = input("\nVui long nhap so dien thoai: ")
        status = -1
        for i in self.DanhBa:
            if(i['phone'] == value):
                print(f"\nName: {i['name']}, Phone: {i['phone']}, Email: {i['email']}")
                status += 1
        if(status == -1):
            print("\nSo dien thoai khong dung, hoac khong ton tai")
    
    def delete_Contact(self):
        print("\n")
        print("-----")
        print("\nXoa lien he")
        value = input("\nVui long nhap so dien thoai can xoa: ")
        status = -1
        for i, data in enumerate(self.DanhBa):
            if(data['phone'] == value):
                self.DanhBa.pop(i) #.pop xóa theo index, .remove là xóa giá trị, dùng cho .remove(data) thì được
                status += 1
                print("\nXoa lien he co so dien thoai: " + str(value) + (" thanh cong !!!"))
        if(status == -1):
            print("\nSo dien thoai khong dung, hoac khong ton tai")
    
    def show_Contact(self):
        print("\n")
        print("-----")
        print("\nHien thi toan bo danh ba")
        print("\n-----")
        for i in self.DanhBa:
            print(f"\nName: {i['name']}, Phone: {i['phone']}, Email: {i['email']}")

class Contact(PhoneBook):
    def __init__(self, name, phone, email, danhBa):
        super().__init__
        self.name = name
        self.phone = phone
        self.email = email
        self.DanhBa = danhBa
        list_contact = {'name': self.name, 'phone': self.phone, 'email': self.email}
        self.DanhBa.append(list_contact)

def rollback(danhBa):
    print("\n")
    print("-----")
    option = input("\nBan co muon tiep tuc su dung chuong trinh (y/n): ")

    if(option == "y"):
        return switch_case(danhBa)
    return 0

def switch_case(danhBa):
    print("\n")
    print("-----")
    print("\nChao mung den voi he thong quan ly danh ba")
    print("\n1. Hien thi toan bo danh ba")
    print("\n2. Them lien he moi")
    print("\n3. Tim kiem lien he")
    print("\n4. Xoa lien he")
    print("\n5. Thoat chuong trinh")

    print("\n-----")
    option = int(input("\nVui long dua ra lua chon cua ban: "))
    match option:
        case 1: 
            danhBa.show_Contact()
            return rollback(danhBa)
        case 2:
            danhBa.add_Contact()
            return rollback(danhBa)
        case 3:
            danhBa.search_Contact()
            return rollback(danhBa)
        case 4:
            danhBa.delete_Contact()
            return rollback(danhBa)
        case 5:
            return 0
def main():
    print("\n")
    danhBa = PhoneBook()
    switch_case(danhBa)
if __name__ == "__main__":
    main()
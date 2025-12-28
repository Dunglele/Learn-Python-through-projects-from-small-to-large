class Note():
    def __init__(self, title, content, id):
        self.title = title
        self.content = content
        self.id = id

    def show(self):
        print(f"\nID: {self.id}, Title: {self.title}")
        print(f"\nContent: {self.content}")

class Notebook():
    def __init__(self):
        self.listNote = []
        self.next_id = 1
    
    def add_Note(self):
        title = input("\nVui long nhap tieu de: ")
        content = input("\nVui long nhap noi dung: ")

        note = Note(title, content, self.next_id)
        self.listNote.append(note)
        print("\nThem note voi ID: " + str(self.next_id) + " thanh cong!!!")
        self.next_id += 1

    def update_Note(self):
        print("\n-----")
        id = int(input("\nNhap ID note muon sua: "))
        found = False
        for data in self.listNote:
            if(data.id == id):
                data.title = input("Nhap tieu de moi: ")
                data.content = input("Nhap noi dung moi: ")
                found = True
                print("Sua ID: " + str(id) + " thanh cong")
        if not found:
            print("\nID khong ton tai, hoac tham so dau vao sai")
    
    def delete_Note(self):
        print("\n-----")
        id = int(input("\nNhap ID note muon xoa: "))
        found = False
        for i, data in enumerate(self.listNote):
            if(data.id == id):
                self.listNote.pop(i)
                found = True
                print("Xoa ID: " + str(id) + " thanh cong")
        if not found:
            print("\nID khong ton tai, hoac tham so dau vao sai")

    def search_Note(self):
        print("\n-----")
        id = int(input("\nNhap ID note muon tim: "))
        found = False
        for i in self.listNote:
            if(i.id == id):
                print("\n-----")
                i.show()
                found = True
        
        if not found:
            print("\nID khong ton tai, hoac tham so dau vao sai")

    def show_Note(self):
        print("\n")
        print("\nDanh sach note")
        print("\n")
        for i in self.listNote:
            i.show()
            print("\n-----")

def rollback(noteBook):
    print("\n-----")
    option = input("Ban co muon tiep tuc su dung chuong trinh (y/n): ")

    if(option == "y"):
        return switch_case(noteBook)
    
    return 0

def switch_case(noteBook):
    print("\n")
    print("-----\n")
    print("Chao mung den voi he thong quan ly Notebook\n")
    print("-----\n")
    print("1. Them ghi chu moi\n")
    print("2. Sua ghi chu\n")
    print("3. Xoa ghi chu\n")
    print("4. Tim kiem\n")
    print("5. Hien thi tat ca\n")
    print("6. Thoat")

    option = int(input("\nVui long cho ra lua chon: "))

    match option:
        case 1:
            noteBook.add_Note()
            rollback(noteBook)
        case 2:
            noteBook.update_Note()
            rollback(noteBook)
        case 3:
            noteBook.delete_Note()
            rollback(noteBook)
        case 4:
            noteBook.search_Note()
            rollback(noteBook)
        case 5:
            noteBook.show_Note()
            rollback(noteBook)
        case 6:
            return 0


def main():
    noteBook = Notebook()
    switch_case(noteBook)

if __name__ == "__main__":
    main()
books = [
    {'id' : 1, 'name' : 'Hello Python', 'author' : 'William James', 'export_year' : 2025},
    {'id' : 2, 'name' : 'C# Language Programing', 'author' : 'Microsoft', 'export_year' : 2020},
    {'id' : 3, 'name' : 'Design UX/UI With Figma', 'author' : 'Quang Dung', 'export_year' : 2026}
]
def list_Book(books):
    print("\n")
    n = 0
    for i in books:
        print(f"ID: {books[n]['id']}, Name: {books[n]['name']}, Author: {books[n]['author']}, Nam xuat ban: {books[n]['export_year']}\n")
        n += 1
    pass

def add_Book(books):
    print("\n")

    id = int(input("ID sach: "))
    name = input("Ten sach: ")
    author = input("Tac gia: ")
    export_year = int(input("Nam xuat ban: "))

    new_book = {'id' : id, 'name' : name, 'author' : author, 'export_year' : export_year}
    books.append(new_book)
    print("\nThem sach thanh cong ^^")
    pass

def update_Book(books):
    print("\n")
    id_anchor = int(input("Nhap id sach ban muon sua: "))
    real_id = -1

    for i, data in enumerate(books):
        if int(data['id']) == id_anchor:
            real_id = i
    if(real_id == -1):
        print("Gia tri dau vao khong hop le, hoac sach khong ton tai")
        return update_Book(books)   

    books[real_id]['id'] = int(input("Nhap id: "))
    books[real_id]['name'] = input("Nhap ten sach: ")
    books[real_id]['author'] = input("Nhap ten tac gia: ")
    books[real_id]['export_year'] = int(input("Nhap nam xuat ban: "))

    print("\nCap nhat sach thanh cong")
    pass

def search_book(books):
    print("\n")
    id_anchor = int(input("Nhap id sach can tim kiem: "))
    real_id = -1
    for i, data in enumerate(books):
        if data['id'] == id_anchor:
            real_id = i
    if(real_id == -1):
        print("Gia tri dau vao khong hop le, hoac sach khong ton tai")
        return search_book(books) 

    print("\nDay la cuon sach ban dang tim ^^")
    print(f"\nID: {books[real_id]['id']}, Name: {books[real_id]['name']}, Author: {books[real_id]['author']}, Nam xuat ban: {books[real_id]['export_year']}")
    pass

def delete_book(books):
    print("\n")
    id_anchor = int(input("Nhap id sach can xoa: "))
    real_id = -1
    for i, data in enumerate(books):
        if data['id'] == id_anchor:
            real_id = i
    if(real_id == -1):
        print("\nGia tri dau vao khong hop le, hoac sach khong ton tai")
        return delete_book(books)

    books.remove(books[real_id])
    print("\nXoa sach co id la " + str(id_anchor) + " thanh cong")
    pass



def switch_case(books):

    print("\n")
    print("Xin chao den voi he thong quan ly sach ^^\n")
    print("1. Xem danh sach\n")
    print("2. Them sach moi\n")
    print("3. Sua thong tin sach\n")
    print("4. Tim kiem sach\n")
    print("5. Xoa sach\n")

    option = int(input("\nXin moi nhap lua chon cua ban: "))

    match option:
        case 1:
            list_Book(books)
            question = input("\nBan co muon tiep tuc su dung (y/n): ")
            if question == "n":
                return 0
            return switch_case(books)
        case 2:
            add_Book(books)
            question = input("\nBan co muon tiep tuc su dung (y/n): ")
            if question == "n":
                return 0
            return switch_case(books)
        case 3:
            update_Book(books)
            question = input("\nBan co muon tiep tuc su dung (y/n): ")
            if question == "n":
                return 0
            return switch_case(books)
        case 4:
            search_book(books)
            question = input("\nBan co muon tiep tuc su dung (y/n): ")
            if question == "n":
                return 0
            return switch_case(books)
        case 5:
            delete_book(books)
            question = input("\nBan co muon tiep tuc su dung (y/n): ")
            if question == "n":
                return 0
            return switch_case(books)
        
switch_case(books)
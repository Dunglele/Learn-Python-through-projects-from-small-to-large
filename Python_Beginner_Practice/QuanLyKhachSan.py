hotels = [
    {'id': 1, 'type_room': 'single', 'price': 2.000, 'status': 'rent'},
    {'id': 2, 'type_room': 'double', 'price': 6.000, 'status': 'rent'},
    {'id': 3, 'type_room': 'single', 'price': 10.000, 'status': 'empty'}
]

def show_room(hotels):
    print("\n")
    print("\n-----")
    for i in hotels:
        print(f"\nID: {i['id']}, Type: {i['type_room']}, Price: {i['price']}, Status: {i['status']}")
    return rollback()

def for_rent(hotels):
    print("\n")
    print("\n-----")
    print("\nDanh sach cac phong chua duoc thue")
    
    for i in hotels:
        if(i['status'] == "empty"):
            print(f"\nID: {i['id']}, Type: {i['type_room']}, Price: {i['price']}, Status: {i['status']}")

    selection = int(input("\nVui long nhap ID phong muon thue: "))
    real_id = -1

    for i, data in enumerate(hotels):
        if(data['id'] == selection):
            real_id = i
    
    if(real_id == -1):
        print("Du lieu dau vao khong hop le, hoac ID khong ton tai!!!")
        input()
        return for_rent(hotels)
    
    hotels[real_id]['status'] = "rent"
    print("Thue phong thanh cong!!!")
    return rollback()

def check_out(hotels):
    print("\n")
    print("\n-----")
    print("\nDanh sach cac phong da duoc thue")

    for i in hotels:
        if(i['status'] == "rent"):
            print(f"\nID: {i['id']}, Type: {i['type_room']}, Price: {i['price']}, Status: {i['status']}")

    selected = int(input("\nVui long nhap ID phong muon tra: "))
    real_id = -1

    for i, data in enumerate(hotels):
        if(data['id'] == selected):
            real_id = i
    
    if(real_id == -1):
        print("Du lieu dau vao khong hop le, hoac ID khong ton tai!!!")
        input()
        return check_out(hotels)
    
    songayo = int(input("Vui long nhap so ngay o: "))
    tongtien = hotels[real_id]['price'] * songayo

    print("\nTong so tien can phai thanh toan la: " + str(tongtien) +("$"))
    input()
    hotels[real_id]['status'] = "empty"
    return rollback()

def rollback():
    print("-----")
    option = input("\nBan co muon tiep tuc su dung chuong trinh (y/n): ")
    if(option == "y"):
        return switch_case(hotels)
    return 0

def switch_case(hotels):
    print("\n")
    print("\n-----")
    print("\nChao mung den voi he thong quan ly khach san")
    print("\n1. Xem danh sach phong")
    print("\n2. Thue phong")
    print("\n3. Tra phong")
    print("\n-----")
    
    option = int(input("\nVui long dua ra lua chon cua ban: "))

    match option:
        case 1:
            show_room(hotels)
        case 2:
            for_rent(hotels)
        case 3:
            check_out(hotels)

switch_case(hotels)
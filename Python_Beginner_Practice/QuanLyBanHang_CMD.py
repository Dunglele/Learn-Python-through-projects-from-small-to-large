products = [
    {'id': 1, 'name': 'Iphone 17 Pro', 'price': 1700, 'amount': 20},
    {'id': 2, 'name': 'Iphone 13', 'price': 1000, 'amount': 15},
    {'id': 3, 'name': 'Iphone 16 Promax', 'price': 1500, 'amount': 39}
]

doanhthu = 0
soluongsp = 0

def rollback():
    question = input("\nTiep tuc su dung chuong trinh (y/n)")
    if question == "y":
        switch_case()
    return 0

def show_products(products):
    print("\n")
    for i in products:
        print(f"\nID: {i['id']}, Name: {i['name']}, Price: {i['price']}, Amount: {i['amount']}")

def add_product(products):
    print("\n")
    print("\n----")

    id = int(input("\nVui long nhap ID san pham: "))

    for i in products:
        if i['id'] == id:
            print("ID san pham da ton tai!!! Vui long thu lai")
            return add_product(products)

    name = input("Ten san pham: ")
    price = int(input("Gia san pham: "))
    amount = int(input("So luong: "))

    new_product = {'id': id, 'name': name, 'price': price, 'amount': amount}
    products.append(new_product)

    print("\nThem san pham co ID: " + str(id) + " thanh cong !!!")

def update_product(products):
    print("\n")
    print("\n----")
    id_anchor = int(input("Vui long nhap ID san pham can UPDATE: "))
    real_id = -1
    
    for i, data in enumerate(products): # Phải sử dụng hàm enumerate cho product để lấy index (i) cùng dữ liệu (data)
        if data['id'] == id_anchor:
            real_id = i

    if real_id == -1:
        print("ID san pham khong ton tai, hoac du lieu dau vao khong hop le!!!")
        return update_product(products)
    
    amount = int(input("Vui long nhap so luong san pham nhap them: "))
    products[real_id]['amount'] += amount
    print("Cap nhat so luong hang thanh cong cho san pham co ID " + str(id_anchor))

def match_one():
    print("\n")
    print("---")
    print("\nChao mung den quan ly kho hang!!!")
    print("\n1. Hien thi danh sach san pham")
    print("\n2. Them san pham moi")
    print("\n3. Cap nhat so luong hang")

    option = int(input("\nVui long dua ra lua chon: "))

    match option:
        case 1:
            show_products(products)
            rollback()
        case 2:
            add_product(products)
            rollback()
        case 3:
            update_product(products)
            rollback()

def payment(products):
    print("\n")
    print("\n----")

    for i in products:
        print(f"\nID: {i['id']}, Name: {i['name']}, Price: {i['price']}, Amount: {i['amount']}")

    print("\n-----")
    print("\nChao mung ban den voi chuc nang ban hang!!!")

    id_product = int(input("\nVui long nhap ID san pham, khach muon mua: "))
    amount_product = int(input("So luong san pham muon mua: "))

    real_id = -1

    for i, data in enumerate(products):
        if(data['id'] == id_product):
            real_id = i
            if(data['amount'] < amount_product):
                print("So luong san pham ton kho khong du de ban, vui long thu lai sau !!!")
                return rollback()
            
    if real_id == -1:
        print("ID san pham khong ton tai, hoac du lieu dau vao khong hop le!!!")
        return payment(products)
    checkout_price = amount_product * products[real_id]['price']

    print("Tong so tien can thanh toan cho don hang la: " + str(checkout_price))
    products[real_id]['amount'] -= amount_product

    global doanhthu #Khai báo biến toàn cục, cho nó gia nhập vào hàm cục bộ
    global soluongsp #Khai báo biến toàn cục, cho nó gia nhập vào hàm cục bộ

    doanhthu += checkout_price
    soluongsp += amount_product
    rollback()

def sum_checkout():

    global doanhthu #Khai báo biến toàn cục, cho nó gia nhập vào hàm cục bộ
    global soluongsp #Khai báo biến toàn cục, cho nó gia nhập vào hàm cục bộ

    print("\n")
    print("\n----")
    print("Tong doanh thu trong ngay hom nay la " + str(doanhthu) + "$ voi " + str(soluongsp) + " san pham duoc ban ra !!!")
    rollback()

def switch_case():
    print("\n")
    print("---")
    print("\nChao mung den he thong quan ly ban hang")
    print("\n1. Quan ly kho hang")
    print("\n2. Chuc nang ban hang")
    print("\n3. Chuc nang thong ke")

    option = int(input("\nVui long dua ra lua chon: "))

    match option:
        case 1:
            match_one()
        case 2:
            payment(products)
        case 3:
            sum_checkout()

switch_case()
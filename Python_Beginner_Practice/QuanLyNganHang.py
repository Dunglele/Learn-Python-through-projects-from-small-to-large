class TaiKhoanNganHang:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.an = account_number
        self.balance = balance
    def show(self):
        print(f"\nChu tai khoan: {self.name}")
        print(f"\nSo tai khoan: {self.an}") 
        print(f"\nSo du: {self.balance}")

class NganHang:
    def __init__(self):
        self.bank = []
    def add_account(self):
        print("\n-----")
        name = input("\nVui long nhap ten chu tai khoan: ")
        account_number = int(input("Vui long nhap so tai khoan: "))
        balance = int(input("Vui long nhap so du: "))
        account = TaiKhoanNganHang(name, account_number, balance)
        self.bank.append(account)
        return 0
        
    def deposit(self):
        print("\n-----")
        account_number = int(input("\nVui long nhap so tai khoan nguoi gui: "))
        found = False
        for i in self.bank:
            if(i.an == account_number):
                print("-----\n")
                print(f"So du hien tai: {i.balance}")
                print("\n-----\n")
                found = True
        if not found:
            print("So tai khoan khong ton tai, hoac tham so dau vao sai")
            return 0
        money = int(input("Vui long nhap tien gui mong muon: "))
        person = int(input("Vui long nhap so tai khoan nguoi nhan: "))
        found_u = False
        for i in self.bank:
            if(i.an == person):
                found_u = True
                for j in self.bank:
                    if(j.an == account_number):
                        balance_virtual = j.balance - money
                        if(balance_virtual <= 0):
                            print("-----")
                            print("\nGiao dich that bai, so du tai khoan khong du")
                            return 0
                        j.balance -= money
                i.balance += money
                break
            
        if not found_u:
                print("-----")
                print("\nGiao dich that bai, khong tim thay so tai khoan nguoi nhan")
                return 0

        print("-----")
        print("\nGiao dich thanh cong")
        return 0

    def show_account(self):
        for i in self.bank:
            print("\n-----")
            i.show()
        return 0
        
def switch_case(bank):
    print("\nChao mung den voi he thong quan ly ngan hang")
    print("\n-----")
    print("\n1. Them tai khoan")
    print("\n2. Giao dich")
    print("\n3. Hien thi tat ca tai khoan")
    print("\n4. Thoat")
    print("\n-----")
    choose = int(input("\nVui long dua ra lua chon cua ban: "))
    match choose:
        case 1:
            bank.add_account()
            option = input("\nBan co muon tiep tuc (y/n: )")
            if(option == "y"):
                switch_case(bank)
            return 0
        case 2:
            bank.deposit()
            option = input("\nBan co muon tiep tuc (y/n: )")
            if(option == "y"):
                switch_case(bank)
            return 0
        case 3:
            bank.show_account()
            option = input("\nBan co muon tiep tuc (y/n: )")
            if(option == "y"):
                switch_case(bank)
            return 0
        case 4:
            return 0

def main():
    bank = NganHang()
    switch_case(bank)

if __name__ == "__main__":
    main()
class Employee:
    def __init__(self, name):
        self.name = name
        self._salary = 0
    @property #Property, giong instance cho phuong thuc Salary dai dien cho _salary, chi cho nguoi dung xem qua Salary
    def salary(self):
        return self._salary
    @salary.setter #Setter, moi gia tri dau vao deu phai duoc rang buoc truoc khi tien hanh cap nhat tren Class
    def salary(self, value):
        if(value < 0):
            print("\nLuong khong the am")
        else:
            self._salary = value
    def calculate_bonus(self):
        self.bonus = 0
    def show(self):
        print(f"\nName: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def calculate_bonus(self):
        self.bonus = self.salary * 25 / 100

class Developer(Employee):
    def calculate_bonus(self, bug_fixed):
        self.bonus = (self.salary * 0.1 + bug_fixed) * 100

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []
    def get_total_salary(self, salary, bonus):
        total_salary = salary + bonus
        print(f"\nBonus: {bonus}, Total: {total_salary}")

def manager(dep_m):
    name = input("Nhap ten 'Manager': ")
    salary = int(input("Nhap luong co ban: "))

    manager = Manager(name)
    manager.salary = salary #Cach goi Setter, Property
    manager.calculate_bonus()
    
    dep_m.employees.append(manager)
def developer(dep_d):
    name = input("Nhap ten 'Developer': ")
    salary = int(input("Nhap luong co ban: "))

    developer = Developer(name)
    developer.salary = salary #Cach goi Setter, Property
    bug_fixed = int(input("So 'bug', Dev da fix duoc: "))
    developer.calculate_bonus(bug_fixed)
    dep_d.employees.append(developer)

def show_list(dep_m, dep_d):
    print("\n==Danh sach Manager==")
    for i in dep_m.employees:
        i.show()
        dep_m.get_total_salary(i.salary, i.bonus)
        print("\n-")
    print("\n==Danh sach Developer==")
    for i in dep_d.employees:
        i.show()
        dep_d.get_total_salary(i.salary, i.bonus)
        print("\n-")
def switch_case(dep_m, dep_d):
    print("\n-----")
    print("\nChao mung den he thong quan ly nhan su HRM")
    print("\n-----")
    print("\n1. Them Manager")
    print("\n2. Them Dev")
    print("\n3. Danh sach nhan vien")
    print("\n4. Thoat")
    print("\n-----")
    choose = int(input("\nLua chon cua ban: "))

    match choose:
        case 1:
            manager(dep_m)
            answer = input("\nDa hoan thanh yeu cau, ban co muon tiep tuc (y/n): ")
            if(answer == "y"):
                return switch_case(dep_m, dep_d)
        case 2:
            developer(dep_d)
            answer = input("\nDa hoan thanh yeu cau, ban co muon tiep tuc (y/n): ")
            if(answer == "y"):
                return switch_case(dep_m, dep_d)
        case 3:
            show_list(dep_m, dep_d)
            answer = input("\nDa hoan thanh yeu cau, ban co muon tiep tuc (y/n): ")
            if(answer == "y"):
                return switch_case(dep_m, dep_d)
        case 4:
            return 0

def main():
    dep_m = Department("Manager")
    dep_d = Department("Developer")
    switch_case(dep_m, dep_d)
if __name__ == "__main__":
    main()
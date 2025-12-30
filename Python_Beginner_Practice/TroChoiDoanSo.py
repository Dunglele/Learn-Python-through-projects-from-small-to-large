import random
class GameDoanSo:
    def __init__(self, phamvi):
        self.so_bi_mat = random.randint(1, phamvi)
        self.so_lan_doan = 0
        self.da_ket_thuc = False
    def kiem_tra_so(self, guess):
        if guess > self.so_bi_mat:
            print("\nBan doan sai roi, so bi mat phai be hon " + str(guess))
        elif guess < self.so_bi_mat:
            print("\nBan doan sai roi, so bi mat phai lon hon " + str(guess))
        elif guess == self.so_bi_mat:
            print("\nBan doan dung roi, so bi mat la " + str(guess))
            self.da_ket_thuc = True
    def chay_game(self):
        print("\nSo bi mat da duoc tao!!!")
        print("\n-----")
        if self.da_ket_thuc == True:
            print("\nDa co loi xay ra")
        while self.da_ket_thuc == False:
            self.so_lan_doan += 1
            choice = int(input("\nLan doan thu " + str(self.so_lan_doan) + " ban chon: "))
            print("-----")
            self.kiem_tra_so(choice)
        return 0
def main():
    print("Chao mung den voi tro choi doan so")
    gameDoanSo = GameDoanSo(10)
    gameDoanSo.chay_game()
if __name__ == "__main__":
    main()
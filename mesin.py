import random
import sys, os
class Account :
    def __init__(self, id, nama='ziiro', pin=123456, saldo=0):
        self.id = id
        self.nama = nama
        self.pin = pin
        self.saldo = saldo
    
    def cekNama(self):
        return self.nama
    
    def cekPin(self):
        return self.pin
    
    def cekSaldo(self):
        return self.saldo

    def topUp(self, nominal):
        self.saldo += nominal

    def menangJudi(self, jumlahMenang):
        self.saldo += jumlahMenang

    def kalahJudi(self, jumlahKalah):
        self.saldo -= jumlahKalah

print("Welcome....")

acc = Account(id)
pin = int(input("Masukan pin anda! : "))
os.system('cls')
if pin != acc.cekPin():
    print("Pin salah")
    exit()
while acc.cekPin() == pin :
    print("Selamat datang", str(acc.cekNama()), "\nSelamat bermain")
    print("1. Cek Saldo")
    print("2. Topup Saldo")
    print("3. Taruhan 1-3")
    print("4. Keluar Program")
    pilihMenu = int(input("Silahkan pilih : "))
    os.system('cls')
    if pilihMenu == 1:
        print("Saldo anda :", acc.cekSaldo())

    if pilihMenu == 2:
        jumlahTopup = int(input("Masukan jumlah yang ingin di topup :"))
        acc.topUp(jumlahTopup)
        print("Saldo anda sekarang :", str(acc.cekSaldo()))
    
    if pilihMenu == 3:
        while True :
            nominal = int(input("Masukan jumlah taruhan :"))
            if acc.cekSaldo() < nominal:
                print("Saldo anda kurang silahkan topup ")
                print("Saldo anda sekarang ", acc.cekSaldo())
                break
            angkaUser = int(input("Masukan angka yang ingin ditebak (1-3) :"))
            angkaRandom = random.randint(1,3)
            print("Angka yang benar adalah :", angkaRandom)

            if (angkaRandom == angkaUser):
                print("Selamat anda menang")
                acc.menangJudi(nominal)
            else :
                print("Anda kalah")
                acc.kalahJudi(nominal)
            print("saldo anda sekarang : ", acc.cekSaldo())
            ulangJudi = str(input("Ingin melanjutkan (Y/N) ? "))
            if ulangJudi.upper() == "Y": #go back to the top
                continue
            break

    if pilihMenu == 4 :
        print("Terima kasih....")
        exit()
    
    print("Ingin melanjutkan ?")
    print("1. Ya")
    print("2. Tidak")
    pilihan = int(input("Silahkan pilih :"))
    os.system('cls')
    if pilihan == 2:
        print("Terima kasih")
        exit()



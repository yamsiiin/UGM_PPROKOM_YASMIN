#Mencetak Menu
def menu():
    print ("Pilih Bentuk 2D")
    print ()
    print ("1. Persegi Panjang")
    print ("2. Lingkaran")
    print ("3. Segitiga")
    print ("4. Keluar")

def persegi():
    print ("Menghitung Luas Persegi Panjang")
    p = int(input("Masukkan Panjang : "))
    l = int(input("Masukkan Lebar : "))
    luas = p*l
    print ("Luas Persegi Panjang adalah ",luas)
    print()
    print ("Coba lagi [Y/N]? ")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def lingkaran():
    print ("Menghitung Luas Lingkaran")
    r = int(input("Masukkan Jari-Jari : "))
    luas = 3.14*(r**2)
    print ("Luas Lingkaran adalah ",luas)
    print()
    print ("Coba lagi [Y/N]? ")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def segitiga():
    print ("Menghitung Luas Segitiga")
    a = int(input("Masukkan Alas : "))
    t = int(input("Masukkan Tinggi : "))
    luas = (a*t)/2
    print ("Luas Segitiga adalah ",luas)
    print()
    print ("Coba lagi [Y/N]? ")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

menu()
while True:
    pilihan = input("Masukkan pilihan (1-4): ")
    if pilihan == "1":
        persegi()
    elif pilihan == "2":
        lingkaran()
    elif pilihan == "3":
        segitiga()
    elif pilihan == "4":
        print("Keluar dari program.")
        break
    else:
        print("pilihan tdk valid, silahkan coba lg!")
menu()
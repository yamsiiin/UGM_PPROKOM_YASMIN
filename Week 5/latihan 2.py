awal=int(input("Masukkan saldo awal\t:"))
sisa=awal  #bila tidak ada pengeluaran
while(True):
    pengeluaran=int(input("Masukkan pengeluaran hari ini(0 untuk keluar):"))
    if pengeluaran==0: #untuk berhenti
        print("Sisa saldo = ",sisa) #sisa bila diberhentikan
    sisa=sisa-pengeluaran
    if sisa<0:
        print("Saldo tidak cukup")
        print("Sisa saldo",sisa+pengeluaran)
        break
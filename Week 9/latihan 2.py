nilai_data=[]

for i in range(1,6):
    nilai=float(input("Masukkan angka ke-{}:".format(i)))
    nilai_data.append(nilai)
    print(nilai_data)

jumlah_data=sum(nilai_data)
rata_data=sum(nilai_data)/5

pilihan=input("Ingin melihat hasil jumlah atau rata-rata: ")
if pilihan=="jumlah":
    print("Jumlah dari nilai datanya adalah: ", jumlah_data)
elif pilihan=="rata-rata":
    print("Rata-rata dari nilai datanya adalah: ", rata_data)
else:
    print("Input tidak valid, masukkan jumlah atau rata-rata")
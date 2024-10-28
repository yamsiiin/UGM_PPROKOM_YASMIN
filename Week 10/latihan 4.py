daftar = [
    [10,15,20],
    [25,30,35],
    [40,45,50]
]

genap=[num for row in daftar for num in row if num%2 == 0]
ganjil=[num for row in daftar for num in row if num%2 != 0]

jumlah_genap= len(genap)
jumlah_ganjil= len(ganjil)

print("Jumlah angka genap:", jumlah_genap, "angka")
print("Jumlah angka ganjil:", jumlah_ganjil, "angka")
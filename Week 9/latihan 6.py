angka=[1, 5, 4, 6, 7, 12, 45, 9, 99, 55, 100, 88, 75, 60]
print(angka)

genap=[]
ganjil=[]

for i in angka:
  if i % 2== 0:
    genap.append(i)
  else:
    ganjil.append(i)

jumlah_genap= len(genap)
jumlah_ganjil= len(ganjil)

print("Ini adalah angka genap:", genap)
print("Jumlah angka genap:", jumlah_genap, "angka")
print("Ini adalah angka ganjil:", ganjil)
print("Jumlah angka ganjil:", jumlah_ganjil, "angka")

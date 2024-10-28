Array1 = [[4,6],
          [1,7]]
Array2 = [[2,3],
          [5,6]]

hasil_penjumlahan = []
hasil_pengurangan = []

for x in range (0,len(Array1)):
    hasil_penjumlahan.append([])
    for y in range (0,len(Array1[0])):
       hasil_penjumlahan[x].append(Array1[x][y] + Array2[x][y])

for x in range(0, len(Array1)):
    hasil_pengurangan.append([])
    for y in range(0, len(Array1[0])):
        hasil_pengurangan[x].append(Array1[x][y] - Array2[x][y])
    
print("Hasil penjumlahan: ", hasil_penjumlahan)
print("Hasil pengurangan: ", hasil_pengurangan)
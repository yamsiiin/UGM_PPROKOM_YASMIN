matriks = []

for x in range (0,2):
    matriks.append([])
    for y in range (0,3):
        matriks[x].append(int(input(f"Masukkan nilai ke-[{x}][{y}] : ")))

for x in range (0,2):
    for y in range (0,3):
        print(matriks[x][y], end=' ')
    print()
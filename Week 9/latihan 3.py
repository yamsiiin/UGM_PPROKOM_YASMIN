nilai = [4, 5, 11, 12, 14, 16, 16, 19]

bilangan_prima = []

for num in nilai:
    if num > 1:  # Bilangan prima harus lebih dari 1
        is_prima = True  # Anggap num adalah bilangan prima
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:  # Jika num dapat dibagi, maka bukan prima
                is_prima = False
                break
        if is_prima:  # Jika tetap dianggap prima, tambahkan ke array
            bilangan_prima.append(num)

# Menghitung jumlah bilangan prima
jumlah_prima = len(bilangan_prima)

# Menampilkan hasil
print("Bilangan prima yang ditemukan:", bilangan_prima)
print("Jumlah bilangan prima:", jumlah_prima)


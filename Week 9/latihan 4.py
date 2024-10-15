nilai=int(input("Masukkan jumlah elemen dalam array: "))
array=list(range(1, nilai + 1))

print("Array: ",array)

n=int(input("Masukkan sebuah angka untuk mencari kelipatannya: "))

kelipatan=[]
for i in array:
    if i % n==0:
        kelipatan.append(i)

if kelipatan:
    print("Elemen yang merupakan kelipatan dari ",n,":",kelipatan)
else:
    print("Tidak ada kelipatan dari",n," dalam array.")


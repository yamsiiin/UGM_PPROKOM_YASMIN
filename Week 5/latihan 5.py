#deklarasi variabel
var_nilai=0
var_i=1
#perulangan FOR
for var_nilai in range (0,10):
    print("Perulangan pertama ke",var_nilai)
    for var_i in range (1,3):
        print("Perulangan ke",var_nilai,",",var_i)
    #diluar perulangan var_i
    var_i=1
#diluar perulangan var_nilai
print("var_nilai=",int(var_nilai)+1,"=10. Bernilai False")
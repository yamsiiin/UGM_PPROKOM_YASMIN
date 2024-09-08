pemain1=str(input("masukkan nilai: "))
pemain2=str(input("masukkan nilai: "))
if(pemain1==pemain2):
    print("Seri")
elif(pemain1=="kertas"):
    if(pemain2=="batu"):
        print("pemain1 menang")
    else: 
        print("pemain2 menang")
elif(pemain1=="gunting"):
    if(pemain2=="kertas"):
        print("pemain1 menang")
    else:
        print("pemain2 menang")
elif(pemain1=="batu"):
    if(pemain2=="gunting"):
        print("pemain1 menang")
    else:
        print("pemain2 menang")
else:
    print("nilai yang anda masukkan salah")

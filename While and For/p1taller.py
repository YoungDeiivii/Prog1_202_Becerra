num=int(input("INGRESE UN NUMERO "))
for i in range(1,num+1):
    if num%i==0:
        print(f"{i} ES DIVISOR")
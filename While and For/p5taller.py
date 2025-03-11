num=1
while num<=1000:
    cont=1
    x=0
    while cont<=num:
        if num%cont==0:
            x=x+1
        cont+=1
    if x==2:
        print(num,end=",")
num+=1

for i in range (1,1001):
    j=2
    sum=0
    while j<=i:
        if i % j == 0:
         sum +=i // j
        j+=1

    if sum == i:
       print(i)
       
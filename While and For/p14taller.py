for num in range(1, 1000):     
    n1 = num // 100       
    n2 = (num // 10) % 10     
    n3 = num % 10             
suma = n1*3 + n2 + n3*3 
if suma == num: 
    print (num,end=",")
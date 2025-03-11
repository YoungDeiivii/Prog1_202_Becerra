num = int(input("DIGITE UN NUMERO "))

primo = True

if num <= 1:
    primo = False
else:
   
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

if primo:
    print(f"{num} ES PRIMO")
else:
    print(f"{num} NO ES PRIMO")
    
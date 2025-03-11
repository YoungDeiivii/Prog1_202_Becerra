num = int(input("INGRESE UN NUMERO "))
i = 1
div = 0
while i < num:
    if num % i == 0:
        div += i
    i += 1

if div == num:
    print(f"EL NUMERO {num} ES PERFECTO")
else:
    print(f"EL NNUMERO {num} NO ES PERFECTO")
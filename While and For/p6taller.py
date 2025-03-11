cont = 0 
while True:
    numero = int(input("INGRESE UN NUMERO "))
    if numero < 0:
        break
    cont += 1  

print("INGRESO", cont,"NUMEROS")
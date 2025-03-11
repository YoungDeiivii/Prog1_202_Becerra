
num1 = int(input("Ingrese el primer numero: ")) 
num2 = int(input("Ingrese el segundo numero: ")) 
 
if num1 > num2:     
    mayor = num1     
    menor = num2 
else: 
    mayor = num2    
    menor = num1 
 
cociente = 0 
residuo = mayor 
 
while residuo >= menor:    
     residuo -= menor    
     cociente += 1 
 
print(f"EL CONCIENTE ES {cociente}") 
print(f"EL RESIDUO ES {residuo}") 

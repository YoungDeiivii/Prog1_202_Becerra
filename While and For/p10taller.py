num1 = int(input("INGRESE UN NÚMERO "))
num2 = int(input("INGRES UN SEGUNDO NÚMERO" )) 
 
while num2 != 0:      num1, num2 = num2, num1 % num2 
print(f"EL MDC ES {num1}") 

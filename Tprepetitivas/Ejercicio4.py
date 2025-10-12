total = 0
num = int(input("Ingrese los numeros: "))
while num != 0:
    total += num
    num = int(input("ingrese un nuevo numero:"))
else:
     print(f"El total es: ", total)
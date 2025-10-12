
total = 0
contador = 100

for i in range(contador):
    num = int(input(f"ngrese 100 numeros enteros{i+1}:"))
    total += num

media = total / contador 
print("la media es:", media)
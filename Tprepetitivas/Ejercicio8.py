
numerospares = 0
numerosimpares = 0
numerosnegativos = 0
numerospositivos = 0

for i in range(100):
    num = int(input("Ingrese 100 numeros enteros: "))

    if num % 2 == 0:
        numerospares +=1
    else:
        numerosimpares +=1

    if num >0:
        numerospositivos +=1
    else:
    
        numerosnegativos +=1

print("Los numeros pares son:", numerospares)
print("Los numeros impares son:", numerosimpares)
print("Los numeros positivos son:", numerospositivos)
print("Los numeros negativos son:", numerosnegativos)
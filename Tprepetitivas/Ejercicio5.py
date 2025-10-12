numero_secreto =5
intentos = 0

num = int(input("Adivine el numero (de 0 a 9): "))

while num != numero_secreto:
    print("ERROR") 
    intentos += 1
    num = int(input("Adivine el numero (de 0 a 9): "))
intentos +=1

print("ADIVINASTE", intentos)
    
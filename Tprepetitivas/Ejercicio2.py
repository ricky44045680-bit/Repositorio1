ent = abs(int(input("Ingrese un numero entero")))

contador = 0


if ent == 0:
    contador = 1
else:
    while ent >0:
        ent = ent // 10
        contador += 1
print("la cantidad de numeros enterons son:", contador)
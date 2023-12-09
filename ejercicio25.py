nPos = 0
nNeg = 0
for x in range (5):
    numero = int(input("Ingrese 5 numeros: "))
    print(numero)
    if numero > 0:
        nPos +=1
    elif numero < 0:
        nNeg +=1
print("Los numeros positivos son: ", nPos)
print("Los numeros negativos son: ", nNeg)
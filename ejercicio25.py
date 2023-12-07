I = 1
nPos = 0
nNeg = 0
nNul = 0

while I <= 100:
    Num = 0
    if Num == 0:
        if Num > 0:
            nPos = nPos + 1
        elif Num < 0:
            nNeg = nNeg + 1
        else:
            nNul = nNul + 1
        I+=1 

print("Los numeros positivos son: ", nPos)
print("Los numeros negativos son: ", nNeg)
print("los numeros nulos son: ",nNul)


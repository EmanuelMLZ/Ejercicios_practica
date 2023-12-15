Suma_gastos = 0
resp = "si"

while resp == "si" :
    print("")
    gastos = float(input("Ingrese los gastos: "))
    Suma_gastos = Suma_gastos + gastos  
    print("")
    print("El total de gastos es: ", Suma_gastos)
    print("")
    print("-Si desea agregar mas gastos responda si: \n-Si desea terminar responda no:\n")
    print("")
    resp = input("")
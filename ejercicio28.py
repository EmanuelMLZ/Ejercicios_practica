resp = "si"
descuento = 0
tcd = 0

while resp == "si":
    print("")
    nombre = str(input("Ingrese su nombre: "))
    compra = float(input("Ingrese el precio de su compra: "))
    color = str(input("Ingrese el color elegido: "))
    print("")
    if color == "rojo":
        descuento = compra * 0.4
        tcd = compra - descuento
    elif color == "amarillo":
        descuento = compra *0.25
        tcd = compra - descuento
    print(nombre)
    print("")
    print("Su total con descuento es: ", tcd)
    print("")
    print("Su descuento es de: ",descuento)
    print("")
    print("-Si desea agregar otro cliente responda si: \n-Si desea terminar responda no: \n")
    resp = input("")
    print("")
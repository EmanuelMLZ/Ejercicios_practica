total = 0
print("\n")
articulo = (input("¿Que articulo desea? :"))
resp = "si"
print("\n")

while resp == "si":
    Num_art = int(input("Ingrese el numero de articulos que desea: "))
    Precio_art = float(input("Ingrese el precio del articulo: "))
    sub_total = Precio_art  *  Num_art
    total = total + sub_total
    print("\n")
    print("- Si desea continuar responda si: \n- Si desea terminar responda no: \n")
    resp = input("")
    print("\n")
    print("Su total a pagar es: ", total)
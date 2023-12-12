total = 0
resp = "si"

while resp == "si":
    print("\n")
    articulo = (input("¿Que articulo desea? : "))
    Num_art = int(input("Ingrese el numero de articulos que desea: "))
    Precio_art = float(input("Ingrese el precio del articulo: "))
    sub_total = Precio_art  *  Num_art
    total = total + sub_total
    total = round(total,2)
    print("\n")
    print("Su total a pagar es: ", total)
    print("\n")
    print("- Si desea continuar responda si: \n- Si desea terminar responda no: \n")
    resp = input("")
    print("\n")
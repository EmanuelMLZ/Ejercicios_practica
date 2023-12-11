total = 0
articulo = print(input("¿Que articulo desea? :"))
resp = "si"

while resp == "si":
    Num_art = int(input("Ingrese el numero de articulos que desea: "))
    Precio_art = float(input("Ingrese el precio del articulo: "))
    sub_total = Precio_art  *  Num_art
    total = total + sub_total
    print("- Si desea continuar responda si: \n- Si desea terminar responda no: \n")
    print(resp)
    print("\n")
    print("Su total a pagar es: ", total)
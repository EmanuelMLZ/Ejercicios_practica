aumento = 0
Nsueldo = 0
nomina_aum = 0
nomina_sueldo = 0
I = 1
for x in range (5):
    print("")
    nombre = str(input("Ingrese su nombre: "))
    codigo = str(input("Ingrese su codigo: "))
    sueldo = float(input("Ingrese su sueldo: "))
    if sueldo < 650:
        aumento = sueldo * 0.15
        Nsueldo = sueldo + aumento
    elif sueldo <= 1000:
        aumento = sueldo * 0.12
        Nsueldo = sueldo + aumento
    else:
        aumento = sueldo * 0.09
        Nsueldo = sueldo + aumento
    print("")
    print("Nombre: " ,nombre, "", "Codigo: " ,codigo, "", "Sueldo actual: ", sueldo)
    print("")
    print("Su nuevo sueldo es: ",Nsueldo)
    print("")
    print("Su aumento de sueldo es de: ",aumento)
    print("")
    nomina_aum = nomina_aum + aumento
    nomina_sueldo = nomina_sueldo + Nsueldo
    I+=1
print("El total de aumentos es: ", nomina_aum)
print("")
print("El total de nomina es: ", nomina_sueldo)
print("")

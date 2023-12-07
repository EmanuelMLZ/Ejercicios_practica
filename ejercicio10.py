can_pay = int(input("cantidad de payasos: "))
can_muñ = int(input("cantidad de muñecas: "))

pes_pay = 112 
pes_muñ = 75 

total_peso_pay = pes_pay * can_pay
total_peso_muñ = pes_muñ * can_muñ

pes_total = total_peso_pay + total_peso_muñ


print("la cantidad de payasos es: " , can_pay)
print("la cantidad de muñecas es: " , can_muñ)
print("el peso total es: " , pes_total)
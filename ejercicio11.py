can_depo = float(input("Ingrese la cantidad depositada: " ))

interes_a = 0.04
gan_total1 = ((can_depo * interes_a) + can_depo)
gan_total2 =  ((gan_total1 * interes_a) + gan_total1)
gan_total3 = ((gan_total2 * interes_a ) + gan_total2 )
print("La ganancia del primer año es:" ,gan_total1) 
print("La ganancia del segundo año es: " ,gan_total2)
print("La ganancia del tercer año es: " ,gan_total3) 

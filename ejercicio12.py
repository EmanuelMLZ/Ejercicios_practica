pan_viejo = int(input("Cantidad de barras de pan viejo: "))

precioPanFresco = 3.49
descuentoPanViejo = 0.060
descuentoDinero  = precioPanFresco  * descuentoPanViejo
valorPanViejo = precioPanFresco - descuentoDinero 
total = valorPanViejo * pan_viejo

print("El precio normal de una barra de pan es:" ,precioPanFresco)
print("El descuento que se le aplica es de: " ,descuentoDinero)
print("El precio total es: " ,total) 

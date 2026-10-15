'''
Calcular el total a pagar por la compra de zapatillas. Si se compran tres  o más zapatillas
se aplica un descuento del 20% sobre el total de la compra y si son menos de tres zapatillas
un descuento del 10%. Mostrar en pantalla, el valor de la compra, el valor
del descuento y el valor a pagar una vez aplicado el descuento.
'''
Compra = float (input("Ingrese la cantidad de zapatos a comprar: "))
Precio = float (input("Ingrese el precio unitario de las zapatillas: "))
Total_Compra = Compra * Precio
if Compra >= 3:
    Descuento = Total_Compra * 0.20
    Total = Total_Compra - Descuento
    print("El valor de la compra es: ", Total_Compra)
    print("El valor del descuento es: ", Descuento)
    print("El valor a pagar es: ", Total)

else:
    
    Descuento = Total_Compra * 0.10
    Total = Total_Compra - Descuento
    print("El valor de la compra es: ", Total_Compra)
    print("El valor del descuento es: ", Descuento)
    print("El valor a pagar es: ", Total)

'''
Una empresa quiere hacer una compra de varias piezas de la misma clase a una fábrica de bolsos.
La empresa, dependiendo del monto total de la compra, decidirá qué hacer para pagar al fabricante: 
    Si el monto total de la compra excede de $500 000 la empresa tendrá la capacidad de invertir
    de su propio dinero un 55% del monto de la compra, pedir prestado al banco un 30%
    y el resto lo pagará solicitando un crédito al fabricante. 

    Si el monto total de la compra no excede de $500 000 la empresa tendrá capacidad de invertir
    de su propio dinero un 70% y el restante 30% lo pagará solicitando crédito al fabricante.
    El fabricante cobra por concepto de intereses un 20% sobre la cantidad que se le pague a crédito. 

    Si el monto total de la compra excede de $1 000 000 la empresa tendra que invertir de su propio
    dinero un 40% del monto de la compra, pedir un prestamo al banco de un 35% y el resto lo pagara
    solicitando un credito al fabricante. El fabricante cobra por concepto de intereses un 32% 
    solo la cantidad que se le pague a credito.

Imprimir el valor invertido de su propio dinero, el valor prestado al banco,
y el valor del crédito solicitado al fabricante, según sea el caso. 
'''

Monto_Compra = float(input("Ingrese el monto total de la compra: "))
if Monto_Compra > 500000:
    Inversion_Propia = Monto_Compra * 0.55
    Prestamo_Banco = Monto_Compra * 0.30
    Credito_Fabricante = Monto_Compra - (Inversion_Propia + Prestamo_Banco)
    print("El valor invertido de su propio dinero es: ", Inversion_Propia)
    print("El valor prestado al banco es: ", Prestamo_Banco)
    print("El valor del crédito solicitado al fabricante es: ", Credito_Fabricante)

elif Monto_Compra > 1000000:
    Inversion_Propia = Monto_Compra * 0.40
    Prestamo_Banco = Monto_Compra * 0.35
    Credito_Fabricante = Monto_Compra * 0.25
    Intereses = Credito_Fabricante * 0.32
    print("El valor invertido de su propio dinero es: ", Inversion_Propia)
    print("El valor prestado al banco es: ", Prestamo_Banco)
    print("El valor del crédito solicitado al fabricante es: ", Credito_Fabricante)
    print("El valor de los intereses a pagar al fabricante es: ", Intereses)

else:
    Inversion_Propia = Monto_Compra * 0.70
    Credito_Fabricante = Monto_Compra * 0.30
    Intereses = Credito_Fabricante * 0.20
    print("El valor invertido de su propio dinero es: ", Inversion_Propia)
    print("El valor del crédito solicitado al fabricante es: ", Credito_Fabricante)
    print("El valor de los intereses a pagar al fabricante es: ", Intereses)
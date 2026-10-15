'''
prendiz aprueba o desaprueba Algoritmia,
sabiendo que aprobará si su promedio de tres calificaciones es mayor o igual a 70;
reprueba en caso contrario
'''
nota_1 = float(input("Ingrese la primera nota: "))
nota_2 = float(input("Ingrese la segunda nota: "))
nota_3 = float(input("Ingrese la tercera nota: "))
promedio = (nota_1 + nota_2 + nota_3) / 3

if promedio >= 70:
    print("El estudiante aprueba Algoritmia.")
else:
    print("El estudiante reprueba Algoritmia.")
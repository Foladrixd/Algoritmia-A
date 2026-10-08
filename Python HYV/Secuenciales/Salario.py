nombre = input("Cual es el nombre del trabajador? ")
mensual = int(input("Ingrese su pago mensual: "))
dias_trabajados = int(input("Ingrese cuantos dias trabajo: "))
horas_trabajados = int(input("ingrese las horas trabajadas: "))
salario = mensual / dias_trabajados
print (nombre, "gana un total de: ", mensual, "por mes, y un total de ", salario, "por dia, trabajando un total de", horas_trabajados, "horas")
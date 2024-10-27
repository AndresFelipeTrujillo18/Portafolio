#EJERCICIO 10
print("PROGRAMA PARA CALCULAR EL SALARIO DE UNA PERSONA")
diario= int(input("Digite el salario diario que obtiene"))
dias = int(input("Digite los dias trabajados"))
op1= diario * dias
porcentaje1= op1 * 0.10
print(f"Se le desconto {porcentaje1} de su salario por el concepto de pension")
porcentaje2 = op1 * 0.25
print(f"Se le desconto {porcentaje2} de su salario por el concepto de salud")
op2= op1 - porcentaje1 - porcentaje2
print(f"Su salario es de {op2} pesos")


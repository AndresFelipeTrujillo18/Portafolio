#Ejercicio 5
nota1 = float(input("Digite su nota "))
nota2 = float(input("Digite su nota "))
nota3 = float(input("Digite su nota "))
nota4 = float(input("Digite su nota "))
nota5 = float(input("Digite su nota "))

promedio = (nota1 + nota2 +nota3 + nota4 + nota5)/5

if promedio >= 3.0:
    print("Aprobo la materia")
else:
    print("Reprobo la materia")
#Ejercicio 2
nombre = input("Digite su nombre ")
edad = int(input("Digite su edad "))

if edad >= 18 and edad<100:
    print(f"{nombre} es mayor de edad")
elif edad < 0:
    print("Ingrese una edad valida")
elif edad > 100:
    print("Ingrese una edad valida")
else:
    print(f"{nombre} eres menor de edad")
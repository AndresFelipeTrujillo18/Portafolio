#Ejercicio 10

llantas = int(input("Digite el numero de llantas que va comprar "))

if llantas < 6:
    total = llantas * 240000
    print (f"El total a pagar es ${total}")
    
elif llantas == 6 or llantas == 7:
    total = llantas * 221000
    print (f"El total a pagar es ${total}")
    
else:
    total = llantas * 180000
    print (f"El total a pagar es ${total}")
    
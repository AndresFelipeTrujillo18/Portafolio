#Ejercicio 12

producto = int(input("Digite la cantidad de productos comprados"))
precio = float(input("Digite el precio unitario del producto"))
if producto <= 5:
    print ("No tiene ningun descuento")
    
elif producto > 5 and producto < 10:
    total = producto * (precio * 0.5)
    print (f"El total a pagar es ${total}")
    
    
elif producto > 10:
    total = producto * (precio * 0.8)
    print (f"El total a pagar es ${total}")
    
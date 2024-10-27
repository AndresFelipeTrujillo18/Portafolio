#Ejercicio 9
menu = """
Tipo de pago
1-Efectivo = pagos menores a $150.000
2-Pago con Celular = pagos entre $150.000 y $300.000
3-Con tarjeta debito = pagos entre $300.000 y $600.000
4-Con tarjeta credito = pagos mayores a $600.000
"""
eleccion = int(input("Digite el metodo de pago el cual desea usar para pagar"))
pago = int(input("Digite el monto que desea pagar"))

if eleccion == 1:
    print("usted ha elegido el metodo de pago en efectivo")

elif eleccion == 2:
    print("usted ha elegido el metodo de pago con celular")

elif eleccion == 3:
    print("usted ha elegido el metodo de pago con tarjeta debito")
    
elif eleccion == 4:
    print("usted ha elegido el metodo de pago con tarjeta credito")
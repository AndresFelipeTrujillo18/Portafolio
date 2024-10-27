#Ejercicio 11
menu = """
Tamaño      Precio
1           $15.000
2           $24.000
3           $36.000

Ingrediente adicional = 4000 (por cada ingrediente)
"""


tamaño = int(input("Ingrese el tamaño de la pizza "))
ingrediente = int(input("Ingrese la cantidad de ingredientes adicionales "))

if tamaño == 1:
    total = 15000 * ingrediente
    print (f"el total a pagar es ${total}")
elif tamaño == 2:
    total = 24000 * ingrediente
    print (f"el total a pagar es ${total}")
else:
    total = 36000 * ingrediente
    print (f"el total a pagar es ${total}")
    
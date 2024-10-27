#Ejercicio 07 

def rango(inicio, numero, final):
    if numero >= inicio and final <= numero:
        print("El numero se encuentra dentro del rango")
        
    else:
        print("El numero no se encuentra dentro del rango")
       
    return inicio, numero, final


    
 
inicio = int(input("Digite el inicio del rango "))
numero = int(input("Digite un un numero "))
final = int(input("Digite el final del rango "))

rango(inicio, numero, final)
   
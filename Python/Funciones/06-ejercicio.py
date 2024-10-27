#Ejercicio 06

def factor(numero):
    if numero <= 0:
        print("El factorial es indefinido (numero negativo)")
    else:
        operacion = 1
        for n in range(1, numero + 1):
            operacion *= n
        return operacion
 

numero = int(input("Digite el digito que desea sacarle factorial "))
print(factor(numero))

#Ejercicio 10
"""
    Determina si un número es primo e imprime el resultado.

    Esta función toma un número entero y determina si es primo o no.
    Imprime un mensaje indicando si el número es primo. Un número primo 
    es aquel que solo es divisible por 1 y por sí mismo. 

    variables de entrada:
    numero (int): El número entero a verificar.

    Devuelve:
    int: El número proporcionado como entrada.

    Ejemplos:
     primo(2)
    El numero es primo
    2
     primo(4)
    el numero no es primo
    4
     primo(5)
    El numero es primo
    5
"""

def primo(numero):
    
    
    if numero <= 1:
        print("el numero no es primo")
    elif numero % 2 == 0 or numero % 3 == 0:
        print ("el numero no es primo")
    elif numero % 4 == 0 or numero % 5 == 0:
        print ("el numero no es primo")
    else:
        print("El numero es primo")
    return numero

numero = int(input("Digite un numero "))

primo(numero)


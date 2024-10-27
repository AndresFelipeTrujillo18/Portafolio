#Ejercicio 01
"""
    Determina el número máximo entre tres números dados e imprime el resultado.

    Esta función toma tres números como argumentos y determina cuál de ellos 
    es el mayor. Luego, imprime el número máximo.

    Entrada:
    numero1 (int, float): El primer número.
    numero2 (int, float): El segundo número.
    numero3 (int, float): El tercer número.

    Devuelve:
    None: La función imprime el número máximo y no devuelve ningún valor.

    Ejemplos:
     maximonumero(10, 20, 30)
    El maximo numero es 30
     maximonumero(10, 40, 20)
    El maximo numero es 40
     maximonumero(50, 20, 10)
    El maximo numero es 50
"""



def maximonumero(numero1, numero2, numero3):
    if numero1 > numero2 and numero1 > numero3:
        maximonumero = numero1
    elif numero2 > numero1 and numero2 > numero3:
        maximonumero = numero2
    else:
        maximonumero = numero3
    print("El maximo numero es ",maximonumero)
    
maximonumero(10, 20, 30)
maximonumero(10, 40, 20)
maximonumero(50, 20, 10)

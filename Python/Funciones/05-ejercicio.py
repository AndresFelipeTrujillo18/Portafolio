#Ejercicio 4
"""
    Calcula la multiplicación de todos los elementos de una lista y imprime el resultado.

    Esta función toma una lista predefinida de números y calcula el producto
    de todos sus elementos. Luego, imprime el resultado y lo devuelve.

    Entrada:
    No hay parámetros de entrada, la función utiliza una lista predefinda.

    Devuelve:
    int, float: El producto de todos los elementos de la lista.

    Ejemplos:
    multiplicacion(lista)
    El resultado es -336
    -336
    """

lista = [8, 2, 3, -1, 7]

def multiplicacion():
    multiplicacion = lista[0] * lista[1] * lista[2] * lista[3] * lista[4] 
    print("El resultado es ",multiplicacion)
    return multiplicacion

multiplicacion(lista)
#Ejercicio 11

def lista_pares(lista):
    lista_pares = []
    for numero in lista:
        if numero % 2 == 0:
            lista_pares += [numero]
            
        else:
            "El numero es impar"
    print(lista_pares)
        

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

lista_pares(lista)
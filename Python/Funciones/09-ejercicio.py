#Ejercicio 09

def elementos(lista):
    lista_unicos = []
    for elemento in lista:

        if elemento in lista_unicos:
            "El numero esta en la lista"
            
        else:
            lista_unicos += [elemento]
            
    print(lista_unicos)
    return lista_unicos


lista = [11, 11, 12, 13, 13, 14, 14, 15, 16, 17, 18, 18, 18, 19, 20]
elementos(lista)


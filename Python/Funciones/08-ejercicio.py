#Ejercicio 08
def mayusculas_minusculas(palabra):
    mayusculas = 0
    minusculas = 0
    
    for letra in palabra:
        if letra.isupper():
            mayusculas += 1
        elif letra.islower():
            minusculas += 1
    print("Número de letras mayúsculas:", mayusculas)
    print("Número de letras minúsculas:", minusculas)
    return mayusculas, minusculas

palabra = str(input("Escriba una palabra con la cantidad de minisculas y mayusculas que desee "))
mayusculas_minusculas(palabra)


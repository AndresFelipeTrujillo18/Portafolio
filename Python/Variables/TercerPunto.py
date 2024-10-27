#PRACTICA EJERCICIO 3
def lineas():
    i = open("poema.txt" , "r", encoding="utf-8")
    #with open("poema.txt" , "w") as archivo:
    lineas = i.readlines()
        
    print(lineas)
    return str(lineas)
    

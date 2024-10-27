#PARCIAL FINAL

import random

import string

nombre_archivo = "PrimerPunto.txt"

caracteres = string.ascii_letters + string.digits  

def contraseña(tamaño):
    combinacion= ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range (tamaño))

    print(combinacion)
    
    with open(nombre_archivo, "a") as archivo:
        archivo.write(combinacion + "\n")
        
    return combinacion

contraseña(9)

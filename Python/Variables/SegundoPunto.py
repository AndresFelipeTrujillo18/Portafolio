archivo_guardado = "SegundoPunto.txt"

def lineas_totales(poema):
    with open(poema, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
    total_lineas = 0
    for i in lineas:
        total_lineas += 1
    return total_lineas

def contar_palabras(poema):
    with open(poema, "r", encoding="utf-8") as archivo:
        texto = archivo.read()
        palabras = texto.split()
    total_palabras = 0
    for i in palabras:
        total_palabras += 1
    return total_palabras

def contar_caracteres(poema):
    with open(poema, "r", encoding="utf-8") as archivo:
        texto = archivo.read()
    total_caracteres = 0
    for i in texto:
        total_caracteres += 1
    return total_caracteres

def contar_palabra_especifica(poema, palabra):
    with open(poema, "r", encoding="utf-8") as archivo:
        texto = archivo.read()
    palabras = texto.split()
    contador = 0
    for i in palabras:
        if i.lower() == palabra.lower():
            contador += 1
    return contador

def procesar_archivo(poema, archivo_salida, palabra):
    total_lineas = lineas_totales(poema)
    total_palabras = contar_palabras(poema)
    total_caracteres = contar_caracteres(poema)
    cuenta_palabra_especifica = contar_palabra_especifica(poema, palabra)

    with open(archivo_salida, "w", encoding="utf-8") as archivo:
        archivo.write(f"Líneas totales: {total_lineas}\n")
        archivo.write(f"Palabras totales: {total_palabras}\n")
        archivo.write(f"Caracteres totales: {total_caracteres}\n")
        archivo.write(f"Cantidad de veces de '{palabra}': en el texto {cuenta_palabra_especifica}\n")


poema = "poema.txt"
palabra = "podrá"  


procesar_archivo(poema, archivo_guardado, palabra)

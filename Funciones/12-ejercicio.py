def palíndromo(palabra):
    palabra_invertida = " "
    for letra in palabra:
        palabra_invertida = letra + palabra_invertida
    print (palabra_invertida)
    return palabra_invertida


palabra = "Anita lava la tina"
palíndromo(palabra)


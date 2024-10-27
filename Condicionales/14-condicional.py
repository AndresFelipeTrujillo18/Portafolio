#Ejercicio 14

edad = int(input("Digite su edad "))

genero = input("Digite su genero ")

if genero == "femenino":
    pulsaciones = (220 - edad) / 10
    print (f"Sus pulsaciones haciendo ejercicio aerobico son de {pulsaciones} pulsaciones cada 10s")
else:
    pulsaciones = (210 - edad) / 10
    print (f"Sus pulsaciones haciendo ejercicio aerobico son de {pulsaciones} pulsaciones cada 10s")
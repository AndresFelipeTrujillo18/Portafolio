#Ejercicio 6
menu = """
1 - Rectangulo
2 - Cuadrado
3 - Paralelogramo
4 - Rombo
5 - Traprecio
6 - Triangulo
7 - Triangulo equilatero
8 - Triangulo rectangulo
9 - Poligono regular
 
"""

num = int(input("Eliga una opcion "))

if num == 1:
    altura = float(input("Digite el valor de la altura en metros "))
    base = float(input("Digite el valor de la base en metros "))
    area1 = altura * base
    print(f"el area del rectangulo es {area1}m²")
elif num == 2:
    lado = float(input("Digite el valor del lado en metros "))
    area2= lado * lado
    print(f"el area del cuadrado es {area2}m²")
elif num == 3:
    altura = float(input("Digite el valor de la altura en metros "))
    base = float(input("Digite el valor de la base en metros"))
    area3 = altura * base
    print(f"el area del paralelogramo es {area3}m²")
elif num == 4:
    diagmayor = float(input("Digite el valor de la diagonal mayor en metros "))
    diagmenor = float(input("Digite el valor de la diagonal menor en metros "))
    area4 = (diagmayor * diagmenor) / 2
    print(f"el area del rombo es {area4}m²")
elif num == 5:
    basemayor = float(input("Digite el valor de la base mayor en metros "))
    basemenor = float(input("Digite el valor de la base menor en metros "))
    altura = float(input("Digite el valor de la altura en metros "))
    area5 = ((basemayor + basemenor)/2) * altura
    
    print(f"El area de un trapecio es {area5}m²")
elif num == 6:
    base = float(input("Digite el valor de la base en metros"))
    altura = float(input("Digite el valor de la altura en metros "))
    area6 = (base * altura)/2
    print(f"el area del triangulo es {area6}m²")
elif num == 7:
    lado = float(input("Digite el valor del lado en metros "))
    raiz = 0.333333
    area7 = ((lado ** 2) * raiz ) / 4
    print(f"el area del triangulo equilatero es {area7}m²")
elif num == 8:
    lado1 = float(input("Digite el valor del lado 1 en metros "))
    lado2 = float(input("Digite el valor del lado 2 en metros "))
    area8 = (lado1 * lado2) / 2
    print(f"el area del triangulo rectangulo es {area8}m²")
elif num == 9:
    perimetro = float(input("Digite el valor del perimetro en metros "))
    apotema = float(input("Digite el valor del apotema en metros "))
    area9 = (perimetro * apotema)
    print(f"El area del poligono regular es {area9}m²")

    
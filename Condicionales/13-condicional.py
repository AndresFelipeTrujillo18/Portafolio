#Ejercicio 13
menu = """
IMC                         Estado
Menor a 18.5                Desnutrido
[18.5 , 25)                 Normal
[25,30)                     Sobrepeso
[30,35)                     Obesidad Grado 1
[35,40)                     Obesidad Grado 2
[40,50)                     Obesidad Grado 3
Mayor o igual a 50          Obesidad Grado 4

"""
peso = float(input("Digite su peso "))
estarura = float(input("Digite su estatura metros "))

IMC = peso/ (estarura ** 2)


if IMC < 18.5:
    print ("Su estado es: Desnutrido ")
    
elif IMC >= 18.5 and IMC <25:
    print ("Su estado es: Normal")
    
elif IMC >= 25 and IMC <30:
    print ("Su estado es: Sobrepeso")

elif IMC >= 30 and IMC <35:
    print ("Su estado es: Obesidad Grado 1")
    
elif IMC >= 35 and IMC <40:
    print ("Su estado es: Obesidad Grado 2")
    
elif IMC >= 40 and IMC <50:
    print ("Su estado es: Obesidad Grado 3")
    
elif IMC >= 50:
    print ("Su estado es: Obesidad Grado 4")
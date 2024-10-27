#Ejercicio 7
menu = """
1 - Fahrenheit a Celsius
2 - Fahrenheit a Kelvin
3 - Fahrenheit a Rankine
4 - Fahrenheit a Réaumur
5 - Celsius a Fahrenheit
6 - Celsius a Kelvin
7 - Celsius a Rankine
8 - Celsius a Réaumur
9 - Kelvin a Celsius
10 - Kelvin a Fahrenheit
11 - Kelvin a Rankine
12 - Kelvin a Réaumur
13 - Rankine a Celsius
14 - Rankine a Fahrenheit
15 - Rankine a Kelvin
16 - Rankine a Réaumur
17 - Réaumur a Celsius
18 - Réaumur a Fahrenheit
19 - Réaumur a Kelvin
20 - Réaumur a Rankine
"""

eleccion = int(input("Digite la opcion: "))

if eleccion == 1:
    dato1 = float(input("Digite la temperatura en Fahrenheit: "))
    temp1 = (dato1 - 32) / 1.8
    print (f"La conversion da {temp1}C°")
    
elif eleccion == 2:
    dato2 = float(input("Digite la temperatura en Fahrenheit: "))
    temp2 = (dato2 + 459.67) / 1.8
    print (f"La conversion da {temp2}K")
    
elif eleccion == 3:
    dato3 = float(input("Digite la temperatura en Fahrenheit: "))
    temp3 = dato3 + 459.67
    print (f"La conversion da {temp3}Ra")
    
elif eleccion == 4:
    dato4 = float(input("Digite la temperatura en Fahrenheit: "))
    temp4 = (dato4 - 32) / 2.25
    print (f"La conversion da {temp4}Re")
    
elif eleccion == 5:
    dato5 = float(input("Digite la temperatura en Celsius: "))
    temp5 = (dato5 * 1.8) + 32
    print (f"La conversion da {temp5}F")
    
elif eleccion == 6:
    dato6 = float(input("Digite la temperatura en Celsius: "))
    temp6 = dato6 + 273.15
    print (f"La conversion da {temp6}K")
    
elif eleccion == 7:
    dato7 = float(input("Digite la temperatura en Celsius: "))
    temp7 = (dato7 * 1.8 ) + 32 + 459.67
    print (f"La conversion da {temp7}Ra")
    
elif eleccion == 8:
    dato8 = float(input("Digite la temperatura en Celsius: "))
    temp8 = dato8 * 0.8
    print (f"La conversion da {temp8}Re")
    
elif eleccion == 9:
    dato9 = float(input("Digite la temperatura en Kelvin "))
    temp9 = dato9 - 273.15
    print (f"La conversion da {temp9}C°")
    
elif eleccion == 10:
    dato10 = float(input("Digite la temperatura en Kelvin "))
    temp10 = (dato10 * 1.8) - 459.67
    print (f"La conversion da {temp10}F")
    
elif eleccion == 11: 
    dato11 = float(input("Digite la temperatura en Kelvin "))
    temp11 = dato11 * 1.8
    print (f"La conversion da {temp11}Ra")
    
elif eleccion == 12: 
    dato12 = float(input("Digite la temperatura en Kelvin "))
    temp12 = (dato12 - 273.15) * 0.8
    print (f"La conversion da {temp12}Re")
    
elif eleccion == 13: 
    dato13 = float(input("Digite la temperatura en Rankine "))
    temp13 = (dato13 - 32 - 459.67) / 1.8
    print (f"La conversion da {temp13}Cº")
    
elif eleccion == 14: 
    dato14 = float(input("Digite la temperatura en Rankine "))
    temp14 = dato14 - 459.67
    print (f"La conversion da {temp14}F")
    
elif eleccion == 15: 
    dato15 = float(input("Digite la temperatura en Rankine "))
    temp15 = dato15 / 1.8
    print (f"La conversion da {temp15}K ")
    
elif eleccion == 16: 
    dato16 = float(input("Digite la temperatura en Rankine "))
    temp16 = (dato16 - 32 - 459.67) / 2.25
    print (f"La conversion da {temp16}Re")
    
elif eleccion == 17: 
    dato17 = float(input("Digite la temperatura en Réameur "))
    temp17 = dato17 * 1.25
    print (f"La conversion da {temp17}Cº")
    
elif eleccion == 18: 
    dato18 = float(input("Digite la temperatura en Réameur "))
    temp18 = (dato18 * 2.25) + 32
    print (f"La conversion da {temp18}F")
    
elif eleccion == 19: 
    dato19 = float(input("Digite la temperatura en Réameur "))
    temp19 = (dato19 * 2.25) + 32
    print (f"La conversion da {temp19}K")
    
elif eleccion == 20: 
    dato20 = float(input("Digite la temperatura en Réameur "))
    temp20 = (dato20 * 2.25) + 32 + 459.67
    print (f"La conversion da {temp20}Ra")
    
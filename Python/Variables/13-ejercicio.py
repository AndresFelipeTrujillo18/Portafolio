#EJERCICIO 13
print("Programa que transforma los segundos en horas y minutos")

num=float(input("Digite los segundos que desea convertir en horas y minutos"))

horas= num // 3600
segundos2= num % 3600
minutos= segundos2 // 60

print(f"{num} son {horas} horas con {minutos} ")

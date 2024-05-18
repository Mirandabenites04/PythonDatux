# 4.Realizar un programa que permita saber si un usario puede obtener un tarjeta de credito
# condiciones : ser mayor de 18 años , un ingreso mensual de 1000 soles mensual.
# si cumple con las 2 condiciones imprimir que tipo de tarjeta puede obtener
# si su ingreso mensual es de 1000 hasta 3000 soles es tarjeta de clasica , mayor a ello tarjeta dorada.
print("INFORMACIÓN NECESARIA PARA OBTENER UNA TARJETA DE CREDITO")
a=input("Ingresa tus Nombres: ")
b=input("Ingresa tus Apellidos: ")
c=int(input("Ingresa tu edad: "))
d=int(input("¿Cuál es tu ingreso mensual? -\n "))
if c<18 or d<1000:
    print(f"sr(a).",a.upper(),b.upper() ,"no cumple con las condiciones para obtener una tarjeta, intentar en la proxima campaña.")
elif d<=3000:
    print(f"sr(a).",a.upper(),b.upper(), " puede obtener su tarjeta de credito clasica.")
else:
    print(f"sr(a).",a.upper(),b.upper() ," puede obtener su tarjeta de credito dorada.")




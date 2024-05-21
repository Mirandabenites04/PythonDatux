OPCIONES_MENU = """
	1)SUMAR
	2)RESTAR
	3)MULTIPLICAR
	4)SALIR
	"""
print("Bienvenido al menu interactivo")
while True:
    opcion= input(OPCIONES_MENU).lstrip() #elimina espacios en blanco5
    if opcion =='1':
        n1= float(input("ingrese el primer número: "))
        n2= float(input("ingrese el segundo número: "))
        suma=n1+n2
        suma=round(suma,0) #redondear numero
        print(f"el resultado de la suma es {suma}")
    elif opcion=='2':
        n1=int(input("introducir el primer número: "))
        n2=int(input("introducir el segundo número: "))
        print(f"El resultado de la resta es {n1-n2}")
    elif opcion== '3':
        n1= float(input("ingrese el primer número: "))
        n2= float(input("ingrese el segundo número: "))
        multiplicación = n1*n2
        print(f"El resultado de la multiplicación es {multiplicación}")
    elif opcion=='4':
        print("¡hasta luego! Ha sido un placer")
        break
    else:
        print("comando desconocido, vuelve a intentarlo")



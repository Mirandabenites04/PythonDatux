print("Bienvenido al menu interativo")
while True:
    print("""¿Qué quieres hacer? Escribe una opción
      1)Saludar
      2)sumar dos números
      3)salir""")
    
    opcion =input( ) # se devuelve un string ''
    if opcion =='1':
        print("Hola, espero que te lo estes pasando bien")
    elif opcion=='2':
        n1=float(input("introduce el primer numero: "))
        n2=float(input("introduce el segundo numero: "))
        print(f"El resultado de la suma es :{n1 + n2}")
    elif opcion=='3':
        print("¡hasta luego! ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentar")
        
    
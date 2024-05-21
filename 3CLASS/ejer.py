print("Bienvenido al menu interativo")
while True:
    print("""¿Que quieres hacer?, Escribe una opción
          1) Saludar
          2)Sumar dos números
          3)Salir""")
    opcion=input( )
    match opcion:
        case "1":
            print("Hola, espero estes bien")
        case "2":
            a1=float(input("ingresa el primer número: "))
            a2=float(input("ingresa el segundo número: "))
            print(f"La suma de los números es = {a1+a2}")
        case "3":
            print("¡hasta luego! ha sido un placer ayudarte")
            break
        case _:
            print("Comando desconocido, vuelve a intentar")
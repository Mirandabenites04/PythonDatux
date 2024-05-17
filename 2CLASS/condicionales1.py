#ejercicio1: mediante un aentrada de teclado determina si una persona puede ser un sugragante
#agregar cuantos años le falta para votar
edad=int(input("Dime cuantos años tienes: "))
if edad>=18:
    print("La persona puede votar")
else:
    print("la persona no puede votar")
    restante =18-edad
    print(f"te falta {restante} años para poder votar")
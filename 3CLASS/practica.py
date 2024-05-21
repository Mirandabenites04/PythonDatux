lista_reseva=[]
nombre =input("ingrese su nombre: ")
telefono =(input("ingrese su numero de telefono: "))
dni =(input("ingrese su numero de dni: "))
ltmp=[nombre, telefono,dni]
lista_reseva.append(ltmp)

blacklist =['79797979','123456']

if ltmp[0][2] in blacklist:
    print("este Dni se encuentra bloqueado")
    lista_reseva ='dnibloqueado'
else:
    print("se puede reservar")
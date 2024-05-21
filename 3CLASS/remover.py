colores=['Rojo','verde','Blanco','Negro','Rosa','amarillo']

if 'negro'in colores:
    indice=colores.index('Negro')
    print(indice)
    colores.remove('negro')
else:
    print("no existe en la lista")

print(colores)
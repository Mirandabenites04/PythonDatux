lista_nombres=['juan', 'antonio','pedro','herminio']
for nombre in lista_nombres:
    print(nombre)
for i,nombre in enumerate(lista_nombres): #sirve para enumerar las opciones
    print(i,nombre)
for indice,nombre in enumerate(lista_nombres):
    print(indice,nombre)
    if nombre == 'juan':
        lista_nombres[indice]='maria' 
print(lista_nombres)

#iteracion sobre diccionarios
d= {'foo':1, 'bar':2 , 'baz':3}
for k, v in d.items():
    key,value=k #desusturcion
    print('k=',k,'v = ', v)
    print(key,value)
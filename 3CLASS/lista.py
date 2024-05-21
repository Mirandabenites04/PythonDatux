numero =[1,2,3,4,5]
print(numero)
a = type(numero)
print(a)

l=['a','e','i','o','u',1,2,3,4,'true']
print(l)
print(l[9]) #buscar el valor en esa ubicación
print(len(numero)) #calcula la cantidad de elementos del vector
lista_vocales = ['a','e','i','o','u']
letter=input("ingrese una vocal: ").lower() #el lower sirve para que pase buscando en toda la lista, sino se quedaria en el primer dato
if letter in lista_vocales:
    print("es una vocal")
else:
    print("no es una vocal")

b=['abc','dfe',False]
c=[1,2,3]
d=['dasd','hola','mundo']
e=[b,c,d]
print (e)

#agrega un dato a la lista ya creada
numero.append('goll')
print(numero)

#cuenta la cantidad de veces que se repite un valor
print(e[0].count(False))

#invertir la lista
print(numero.reverse())

#eliminar un elemento de la lista
print(numero.remove('goll'))

#llamar elementos de una lista determinada
print(numero[0:2])
print(numero[0:5:2])#El 2 dice que tienes que ir saltando de dos en dos elementos
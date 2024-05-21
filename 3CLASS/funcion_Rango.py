#range -> no es una lista
#si quieres convertir en rango en una lista se debe hacer
print([*range(10)])#empieza desde el 0
print([*range(1,11)])#empieza desde el 1 y uno antes del ultimo número
print([*range(0,100,10)])#salta de 10 en 10

for year in range (2001,2013):
    print(f"Informes del año {year}")
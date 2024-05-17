##cadena
#concatenar
msg="Hola"
persona="Alumno"
msgTotal=msg + persona
msgTotalv2="Hola" + "Alumno"
msgTotalv3=msg + "Alumno"
print(msgTotal)
print(msgTotalv2)
print(msgTotalv3)
#Errores
msg2= "HI"
a=10
#msgTotalError=msg2+a
msgTotalErrorv2=msg2*a #asi funciona!!
print(msgTotalErrorv2)
#Funcion de las cadenas(str)
#len => Obtiene la cantidad de caracteres
size=len(msgTotal)
print(size)
#Transformar una variable a cadena
new_str=str(a)
msgTotalFix=msg2+new_str
print(msgTotalFix)


#Operaciones Numericas
c=10
d=8
#operaciones basicas
suma=c+d
resta=c-d
multiplicacion=c*2
exponencial=c**d
division_normal=c/d
division_entera=d//c
print(suma, resta, multiplicacion, division_normal, division_entera)
#operaciones modulo (%)
#es el resto de una división
#d%c => 7%2 => 7 = 2*3 + 1
#157%3 => 157/3 = 3*52 + 1
resto = d%c
print(resto)
#convertir a un entero en un flotante
strnumero='15'
print(type(strnumero))
e=int(strnumero)
print(type(e),e)
#en python se puede hacer operaciones combinadas
f= (3+2/(2*5))**2
print(f)


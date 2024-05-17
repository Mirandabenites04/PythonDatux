#crea una calculadora de impuestos
print("Calculadora de impuestos de Renta")
nombre=input("ingrese su Nombre: ")
salario =float(input("ingrese su salario"))
tax=0
if salario>=0 and salario<=10000:
    tax=5
elif salario>10000 and salario<=25000:
    tax=8
elif salario>25000 and salario<=40000:
    tax=10
else:
    tax=15
#calculadora
impuestos_pagar=(salario*tax)/100
print(f"estimado {nombre} usted debe pagar en el año un impuesto de {impuestos_pagar}")



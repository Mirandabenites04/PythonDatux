# 2. Ingrese un valor por teclado e imprima el tipo de dato
print("Ingresa un valor para poder identificarlo: ")
a=None           #ingresar el valor en lugar de none, ya que si lo trabajamos con print todo los valores nos saldran str
b=type(a)
print(f"El valor {a} es de tipo {b}")
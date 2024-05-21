#definición
#def mi_función():
#    pass #uso del pass es opcional que ayuda a tener una funcion en cuenta
#    return NotImplementedError
def saludar():
    print("hello")

#call o llamar o invocar
print(saludar())

def saludar2(name):
    name="carlos"
    print(f"hello {name} ")
print(saludar2("carlos"))
print(saludar2("juan"))

def saludarv3(name):
    return f"Hello"+ name

namev1=saludarv3('name escogido')
print(namev1)
listaPersonas=[]
dictpersonas={
        "nombre":" ",
        "dni": " ",
        "cursos":" "
}

def statuspersona(age):
    year =2024
    if year - age <18:
        return False
    else:
        return True

def agregarpersona():
    nombre=input("ingrese su nombre")
    dni=input("ingresar su dni")
    cursos=int(input("ingrese cantidad de cursos"))
    dictpersonas['nombre']=nombre
    dictpersonas['dni']=dni
    dictpersonas['cursos']=[]
    for _ in range(cursos):
        namecurso=input("ingrese su curso")
        dictpersonas['cursos'].append(namecurso)
    listaPersonas.append(dictpersonas)

edad= int (input(" Ingrese su fecha de nacimiento"))
status = statuspersona(edad)
while status:
    if status:
        print("Bienvenido a DATUX")
    else:
        print("persona menor de edad")



    msg=""""
    1. Ingresar datos de nuevo alumno
    2. Mostrar alumnos
    """
    print(msg)
    opcion =input("Ingrese su opción:")
    if opcion == 1:
        agregarpersona( )
    elif opcion == 2:
        for i in listaPersonas:
            print(f"la persona con nombre{i['nombre']} esta matriculado en {len(i['cursos'])}cursos")
    else:
        print("ingrese opcion correcta")
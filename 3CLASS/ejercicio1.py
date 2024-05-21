dictAlumno={
    'nombre':'',
    'dni': '',
    'cursos':[]
}
listaalumnos=[]
print("bienvenido a Datux")
nombre=input("ingrese su nombre:")
dni=input("ingrese su dni: ")
cursos=int(input("ingrese cantidad de cursos: "))

dictAlumno['nombre']=nombre
dictAlumno['dni']=dni
dictAlumno['cursos']=cursos
listaalumnos.append(dictAlumno)
print(listaalumnos)
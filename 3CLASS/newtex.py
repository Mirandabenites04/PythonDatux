texto= 'Hola Mundo'
new_text= ''
for letra in texto:
    if letra =='o':
        new_text+='x'
        continue
    new_text += letra
    print(letra)
print(new_text)

texto_s =''
for l in texto:
    texto_s += l
    print(texto_s)
print(texto_s)
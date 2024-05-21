letter=input("ingresa una vocal: ").upper()

if   letter =='A':
    print("es la vocal a")
elif letter =='E':
    print("es la vocal e")
elif letter=='I' or letter()=='O' or letter()=='U':
    print("es la vocal ")
else:
    print("no es una vocal")

match letter:
    case 'A':
        print ("es la vocal A")
    case 'E':
        print("es la vocal E")
    case _:
        print("no es una vocal")
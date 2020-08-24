#prográmek, který napíše slovo nebo větu pozpátku.
print ("Obraceč slov")
slovo = input("Napiš slovo ")
delka = len(slovo)
delka=delka-1
noveslovo=slovo[delka]


while delka>0:
       delka=delka-1
       noveslovo=noveslovo+slovo[delka]
        
print(noveslovo)
list(noveslovo)
print(noveslovo)
noveslovo.insert(2,"b")
print(noveslovo)

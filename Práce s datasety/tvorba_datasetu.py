#Skript vytvoří náhodný dataset pro následné cvičení.
import random
from random import randrange
import json
oblast=["Praha","Brno","Ostrava","Olomouc","Zlin"]
druh=["Tesarik krovovy","Tesarik pizmovy","Patericek zluty","Zlatohlavek zlaty","Rohac obecny"]
pocet=0
error=1
while error == 1:
    try:
        cil=int(input("Zadej počet náhodně vygenerovaných záznamů "))
        oblasti=[]
        vyskyty=[]
        druhy=[]
        while pocet < cil:
            rand_oblast=random.choice(oblast)
            oblasti.append(rand_oblast)
            rand_druh=random.choice(druh)
            druhy.append(rand_druh)
            vyskyt=randrange(0,20)
            vyskyty.append(vyskyt)
            pocet=pocet+1

        celek=[]
        zaznam=0
        delka=len(oblasti)
        while zaznam < delka:
            druh_n=druhy[zaznam]
            oblast_n=oblasti[zaznam]
            vyskyt_n=vyskyty[zaznam]
            lokace={"Druh": druh_n,"Oblast": oblast_n,"Vyskyt":vyskyt_n,"Lokace":zaznam}
            celek.append(lokace)   
            zaznam=zaznam+1




        with open ("././/zaznamy.json", "w") as file:
            json.dump(celek, file)
        error=0
        print("Bylo vygenerováno",cil,"záznamů")
    except ValueError:
        print("Neplatná hodnota")
        error=1
    

    


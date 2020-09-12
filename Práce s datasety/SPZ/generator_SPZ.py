from random import randrange
import random
import json
pocet=int(input("Počet SPZ "))
pismena=["A","B","C","E","H","J","K","L","M","P","S","T","U","Z"]
abc=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
soupis=[]
celkem=0
while celkem < pocet:
    auto={}
    vyber=["pismeno","cislo"]
    volba=random.choice(vyber)
    prvni_cislo=randrange(1,9)
    ctyri_cisla=randrange(1000,9999)
    if volba=="pismeno":
        cislo=randrange(0,9)
        treti=str(cislo)
    else:
        treti=random.choice(abc)
    ipc=str(prvni_cislo)
    icc=str(ctyri_cisla)
    pismeno=random.choice(pismena)
    SPZ=ipc+pismeno+treti+"-"+icc
 
    celkem=celkem+1
    speed=randrange(30,70)

    auto["SPZ"]=SPZ
    auto["Rychlost"]=speed
    soupis.append(auto)

komplet=(json.dumps(soupis, indent=2))
print(komplet)

with open ("././/soupis_SPZ.json", "w") as file:
    json.dump(soupis, file)

#Je třeba nejprve vygenerovat dataset ve skriptu "tvorba_datasetu
import json
with open ("zaznamy.json") as f:
           data = json.load(f)

num=0
delka=(len(data))
unikat=[]
while num < delka:
    lokace=data[num]
    lokace1=lokace["Oblast"]
    if lokace1 not in unikat:
        unikat.append(lokace1)
    num=num+1
print("města na výběr", unikat)
mesto=input("zvol si město ")
zachyt=[]
num=0
while num < delka:
    lokace=data[num]
    lokace_b=lokace["Oblast"]

    if lokace_b == mesto:
        jedinec=(lokace["Druh"])
        zachyt.append(jedinec)

    num=num+1
druhy=[]
length=len(zachyt)
num=0
while num < length:
    druh=zachyt[num]
    if druh not in druhy:
        druhy.append(druh)
    num=num+1
    

pocet_zachytu=[]
delka=len(druhy)
num=0
while num < delka:
    a=druhy[num]
    pocet=zachyt.count(a)
    jedinci=[a,pocet]
    pocet_zachytu.append(jedinci)
    
    num=num+1
print(pocet_zachytu)
    

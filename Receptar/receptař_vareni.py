import json
with open ("recepty.json") as f:
           recepty = json.load(f)
with open ("suroviny.json") as f:
           suroviny = json.load(f)

volby=[]
for i in recepty:
    volby.append(i)
delka=len(volby)
celkem=0
print("Máš na výběr z", volby)
jidlo=input("Co chceš vařit? ")
while celkem < delka:
    volba=volby[celkem]
    if volba == jidlo:
        recept=jidlo
    if jidlo not in volby:
        print("to tu nemám, zkus to ještě jednou")
        jidlo=input("Co chceš vařit? ")
        while celkem < delka:
            volba=volby[celkem]
            if volba == jidlo:
                recept=jidlo
            if jidlo not in volby:
                print("to tu nemám, zkus to ještě jednou")
            celkem=celkem+1
    celkem=celkem+1

veci=[]

for i in recepty[recept]:
    veci.append(i)

celkem=0
delka_veci=len(veci)
sada=(recepty[recept])
suro=[]
for i in suroviny:
    suro.append(i)
delka_suro=len(suro)
print(suro)
suroviny_nove=[]
while celkem < delka_veci:
    sur1=(veci[celkem])
    sady=sada[sur1]
    sur_celkem=0
    while sur_celkem < delka_suro:
        sur2=suro[sur_celkem]
        if sur2==sur1:
            surove={}
            
            mass=(suroviny[sur2])
            nova_mass=mass-sady
            print(nova_mass)
            surove[sur1]=nova_mass
            
            suroviny_nove.append(surove)
            
        sur_celkem=sur_celkem+1
    
    
    celkem=celkem+1

print(suroviny_nove)

with open ("././/surovinys.json", "w") as file:
    json.dump(suroviny_nove, file)

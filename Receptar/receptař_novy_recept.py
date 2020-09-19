import json
with open ("recepty.json") as f:
           data = json.load(f)

recepty=data
print(recepty)


jedna=int(input("Pro založení nového receptu stiskni 1 "))
suroviny=[]
množství=[]
surovina="nic"
if jedna == 1:
    nazvy=input("Napiš název nového receptu ")

    while True:
        surovina=input("Napiš název suroviny/pokud už nechceš nic vložit stiskni enter ")
        if surovina == "":
            break
        suroviny.append(surovina)
        mass=int(input("Množství suroviny v gramech, mililitrech nebo kusech "))
        množství.append(mass)
nazev={}
print(suroviny[0])
print(množství[0])
delka=(len(suroviny))
pozice=0
while pozice < delka:
    
    sur=suroviny[pozice]
    mno=množství[pozice]
    nazev[sur]=mno
    pozice=pozice+1
  
recepty[nazvy]=nazev
print(recepty)

with open ("././/recepty.json", "w") as file:
    json.dump(recepty, file)



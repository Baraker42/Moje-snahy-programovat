import json

try:
    with open ("suroviny.json") as file:
        data=json.load(file)
    ans=input("Přejete si vypsat aktuálně dostupné suroviny?")
   
   
    if ans == "ano" or ans == "Ano" or ans == "ANo" or ans == "ANO":
        for i in data:
            print(i)
            
        ans2=input("Přejete si upravit nějakou existující surovinu? ")
        if ans2 == "ano" or ans2 == "Ano" or ans2 == "ANo" or ans2 == "ANO":
                delka=len(data)
                celkem=0
                material=[]
                while celkem < delka:
                    sur=data[celkem]
                    
                    for i in sur:
                        material.append(i)
                    celkem=celkem+1
                print(material)
                ans3=input("Kterou? ")
                if ans3 in material:
                    delka=len(data)
                    celkem=0
                  
                    while celkem < delka:
                            sur=data[celkem]
                            try:
                                sur1=sur[ans3]
                                print(sur1)
                                celkem=celkem+1
                            except KeyError:
                                celkem=celkem+1

                    
except FileNotFoundError:
    save=False
surovina="nic"
celkove_suroviny=[]
while True:
    suroviny={}
    surovina=input("Vlož novou surovinu do spíže nebo stiskni enter pro ukončení ")
    if surovina=="":
        break
    try:
        mass=int(input("Kolik je dané suroviny? "))
    except ValueError:
        print("Nezadali jste číslo")
        mass=int(input("Kolik je dané suroviny? "))
    suroviny[surovina]=mass
    
    celkove_suroviny.append(suroviny)
    
print(celkove_suroviny)
with open ("././/suroviny.json", "w") as file:
   json.dump(celkove_suroviny, file)

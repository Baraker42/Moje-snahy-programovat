import json
def nahled_receptu(): #Tato funkce umožňuje náhledy do již existujících receptů
    try:
        with open ("recepty.json") as f:
                   data = json.load(f)
        receptar=[]
        for i in data:
            
            receptar.append(i)
        print(receptar)

        while True:
            nahled=input("Který recept si chceš prohlédnout? ")
            try:
                view=data[nahled]
                print(view)
                break
            except KeyError:
                print("Takový recept tu nemám, zkus to ještě jednou")
    except FileNotFoundError: # Pokud dosud neexistuje složka recepty, upozorní uživatele, že musí nejprve nějaký recept založit
        print("Zatím nemám v databázi žádný recept. Nějaký nahraj a zkus to pak")


def novy_recept(): #Spustí tvorbu nového receptu
    suroviny=[]
    množství=[]
    surovina="nic"
    nazvy=input("Napiš název nového receptu ")
    while True:
        surovina=input("Napiš název suroviny/pokud už nechceš nic vložit stiskni enter ")
        if surovina == "":
            break
        suroviny.append(surovina)
        mass=int(input("Množství suroviny v gramech, mililitrech nebo kusech "))
        množství.append(mass)
    nazev={}
    delka=(len(suroviny))
    pozice=0
    while pozice < delka: 
        sur=suroviny[pozice]
        mno=množství[pozice]
        nazev[sur]=mno
        pozice=pozice+1
    try:
        with open ("recepty.json") as f:
           data = json.load(f)
        recepty=data
        recepty[nazvy]=nazev
    except FileNotFoundError:
        recepty={}
        recepty[nazvy]=nazev
    with open ("././/recepty.json", "w") as file:
        json.dump(recepty, file)
    print("Výborně! Nový recept",nazev,"byl uložen")

def uprava_surovin(): #Umožňuje upravit stávající množství surovin nebo přidat suroviny nové
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
        

    with open ("././/suroviny.json", "w") as file:
       json.dump(celkove_suroviny, file)
def vareni(): #Spustí proces "vaření". Po zadání receptu odečte ze surovin množství, které bylo pro vaření potřeba.
    try:
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
    except FileNotFoundError:
        print("Nemůžeš se pustit do vaření, protože tu nemám žádný recept")



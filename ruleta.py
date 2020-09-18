from random import randrange
print ("""Zjednodušená verze hazardní hry Ruleta. Umožňuje vsadit na libovolný počet
čísel a jednu barvu. Neumožňuje sázky na řady a sloupce""")
penize = 500
ANO=["ano","ANO","Ano","aNO","ANo"]
barvy=["Černá","Červená"]
pokracovat="Ano"
while penize >= 0:
    vsazena_cisla=[]
    sazky_na_cisla=[]
    vsazene_barvy=[]
    sazky_na_barvy=[]
    volba=input("Chceš vsadit na číslo? ")
    while pokracovat in ANO:
        if volba in ANO:
            try:
                cislo=int(input("Napiš číslo  (1-37): "))
                if cislo >37 or cislo < 1:
                    print("Na dané číslo nelze vsadit")
                    continue
                vsazena_cisla.append(cislo)
                try:
                    sazka=int(input("Kolik chceš vsadit "))
                    if sazka > penize:
                        print("Tolik peněz nemáš")
                    sazky_na_cisla.append(sazka)
                    penize=penize-sazka
                except ValueError:
                    print("To není číslo, zkusme to znovu")
                    try:
                        sazka=int(input("Kolik chceš vsadit "))
                        if sazka > penize:
                            print("Tolik peněz nemáš")
                        sazky_na_cisla.append(sazka)
                        penize=penize-sazka
                    except ValueError:
                        print("S tebou je to složitý")
                        break
            except ValueError:
                print("To není číslo")
                continue
            pokracovat=input("Chceš vsadit na další? ")
        if volba not in ANO:
            break
    print(vsazena_cisla)
    pokracovat="Ano"
    volba=input("Chceš vsadit na barvu? ")
    if volba in ANO:
        barva=input("Chceš vsadit na Černá nebo Červená? ")
        while barva not in barvy:
            barva=input("Zkus to znovu. Černá nebo Červená ")
        vsazene_barvy.append(barva)
        try:
            sazka=int(input("Kolik chceš vsadit "))
            if sazka > penize:
                print("Tolik peněz nemáš")
            sazky_na_barvy.append(sazka)
            penize=penize-sazka
        except ValueError:
            print("To není číslo, zkusme to znovu")
            try:
                sazka=int(input("Kolik chceš vsadit "))
                if sazka > penize:
                    print("Tolik peněz nemáš")
                sazky_na_barvy.append(sazka)
                penize=penize-sazka
            except ValueError:
                print("S tebou je to složitý")
                break
    print(vsazene_barvy)
    ruleta= randrange(0,37)
    if ruleta % 2 == 0:
        barva = "Červená"
    else:
        barva = "Černá"
    print("Vyhrává číslo ", ruleta, " a barva je", barva)
    if ruleta in vsazena_cisla:
        print("Vyhráváš na vsazené číslo!")
        delka=len(sazky_na_cisla)
        celkem=0
        celkem_sazky=0
        while celkem < delka:
            cislo=vsazena_cisla[celkem]
            if cislo == ruleta:
                while celkem_sazky <= celkem:
                    sazka=sazky_na_cisla[celkem_sazky]
                    if celkem_sazky == celkem:
                        vyhra=sazka*35
                        print(vyhra)
                        penize=penize+vyhra
                    celkem_sazky=celkem_sazky+1
            celkem=celkem+1
            celkem_sazky=0
    elif barva in vsazene_barvy:
        print("Vyhráváš na vsazenou barvu!")
        vyhra=sazka_na_barvy[0]
        vyhra=vyhra*2
        penize=penize+vyhra
    else:
        print("Tentokrát to nevyšlo")
    print("Aktuálně máš",penize)
    

            
        
        

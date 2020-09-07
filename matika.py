#Počítací "hra". Hráč má psát správné výsledky na základě zadání počítače. Počítač vyhodnotí strávnost výsledku
#a připočte body. Při chybě nebo ukončení ze strany hráče, uloží výsledek do souboru score.
import json
from random import randrange
chyba=0
body=0
if True:
    try:
        with open ("score.json") as f:
            data = json.load(f)
        grog=data[0]
        hraci=[]
        for i in grog:
            
            hraci.append(i)
        prev_score=[]
        delka=len(hraci)
        counter=0
        while counter <delka:
            hrac=hraci[counter]
            score_hrace=grog[hrac]
            prev_score.append(score_hrace)
            counter=counter+1
        
        save=True
    except FileNotFoundError:
        save=False
        
        
    




               
while chyba == 0:
    cislo1=randrange(0,101)
    cislo2=randrange(0,101)
    vys=cislo1+cislo2
    print(cislo1,"+",cislo2)
    try:
        odpoved=int(input("Napiš výsledek, případně stiskni enter pro ukončení hry "))
    except ValueError:
        break
            
    if odpoved == vys:
        body=body+1
        print(odpoved,"je správná odpoveď")

    else:
        print(odpoved, "je špatně. Správně je", vys)
        break
print("Počet bodů je:", body)
jmeno=input("Zadej své jméno ")
celkovescore=[]
score={}
score[jmeno]=body
if save == True:
    counter=0
    delka=len(hraci)
    while counter <delka:
        hrac=hraci[counter]
        point=prev_score[counter]
        score[hrac]=point
        counter=counter+1

celkovescore.append(score)


with open ("././/score.json", "w") as file:
    json.dump(celkovescore, file)

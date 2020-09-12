#Počítací "hra". Hráč má psát správné výsledky na základě zadání počítače. Počítač vyhodnotí strávnost výsledku
#a připočte body. Při chybě nebo ukončení ze strany hráče, uloží výsledek do souboru score.
import json
from random import randrange
chyba=0
body=0
celkovescore=[]


if True:
    try:
        with open ("score.json") as f:
            data = json.load(f)
        celkem=0
        delka=len(data)
        print("Highscores")
        for i in data:
            print(i)
        while celkem<delka:
            data1=(data[celkem])
            celkovescore.append(data1)
            celkem=celkem+1        
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

score={}
score["Jmeno"]=jmeno
score["Body"]=body


celkovescore.append(score)
def pocet_bodu(hrac):
    return hrac.get('Body')
celkovescore.sort(key=pocet_bodu, reverse=True)
delka=len(celkovescore)
if delka >= 10:
    celkovescore.pop()
    

print("Highscores")
for i in celkovescore:
    print(i)
    
with open ("././/score.json", "w") as file:
    json.dump(celkovescore, file)


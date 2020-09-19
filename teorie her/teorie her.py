import random
from random import randrange
from ppth import copycat, hustler, jesus, idk, johnwick
a=copycat
b=hustler
c=jesus
d=idk
e=johnwick
kybl=[a,b,c,d,e]

while True:
    ans=input("Chceš hrát dál? ")
    if ans == "ano" or ans == "Ano" or ans =="ANO" or ans =="ANo":
        score=0
        score_pc=0
        pocitadlo=0
        karma=0
        karmaplus=0
        balik=random.choice(kybl)
        while pocitadlo !=10:
            ans=input("(P)odvést/(N)epodvést " )
            
            tah_pc=(balik(karma,karmaplus))
            if ans == "P" and tah_pc=="N":
                score=score+10
                karma=1
            if ans == "N" and tah_pc=="N":
                score=score+5
                score_pc=score_pc+5
                karma=0
            if ans == "P" and tah_pc=="P":
                karma=1
            if ans == "N" and tah_pc=="P":
                score_pc=score_pc+10
                karma=0
            karmaplus=karmaplus+karma
            print(karmaplus)
            print(ans, tah_pc)
            print("Karma",karma)
            print("Tvoje skóre",score, "Skóre PC", score_pc)
            pocitadlo=pocitadlo+1
            if pocitadlo==10:
                if score_pc >=30:
                    kybl.append(balik)
                    if len(kybl) >=20:
                        cislo=randrange(0,20)
                        kybl.pop(cislo)
    else:
        a=input("opravdu ne?")
        if a != "ano":
            print("Ale byla to sranda, ne?")
            break
                

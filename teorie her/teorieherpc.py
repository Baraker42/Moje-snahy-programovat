import random
from random import randrange
from coppycac import copycat, hustler, jesus, idk, johnwick
a=copycat
b=hustler
c=jesus
d=idk
e=johnwick
print("""
Vítejte v simulátoru Teorie Her. Tento simulátor si bere za úkol přiblížit, jak jedna část teorie
her vlastně funguje. Konkrétně se zabývá altruismem, tedy na první pohled nezjištnou pomocí.
Můžeme si to ukázat na příkladu, kdy si dvě opice chtějí navzájem podrbat záda. Tato jednoduchá situace
má několik rozdílných východisek. Obě opice si navzájem podrbou záda, jsou spokojené, ale každou to
stálo čas a energii. Pokud si jedna opice záda podrbat nechá, ale sama u druhé opice očistu neprovede
získá úlevu, ale o žádný čas a energii nepříjde, tím pádem je její zisk vyšší. Pokud si navzájem vůbec
nevyhoví, žádná opice nemá žádný zisk.
""")
input()
print("""
K tomu se může vázat celá řada různých přístupů v našem případě odlišných strategií.V tomto simulátoru se nachází
5 odlišných strategií. Pojďme si ukázat, jak se od sebe liší.
""")
input()
print("""
První představenou strategií je Jesus. Toto označení jsem vybral kvůli její mírumilovnosti. Ať se stane
cokoliv, jedinec s touto strategií v budoucnu vždy pomůže.
""")
input()
print("""
Druhá varianta je CopyCat. Pokud ji někdo zradí, příště už nepomůže, pokud si to druhý jedinec nevyžehlí
""")
input()
print("""
Třetí varianta je John Wick. Jak je z názvu jasné jedná se o referenci na filmovou postavu. Je mírumilovný
dokud ho někdo nezradí. Od té doby neodpouští. Vyžehlit se to nedá.
""")
input()
print("""
Čtvrtá varianta je Hustler. Podvodník. Jediné na co se u něj můžete spolehnout, že nikdy nepomůže. Nikdy.
""")
input()
print("""
Poslední strategií je I don´t know (IDK) neboli Já nevím. Jedinec s touto strategií pomáhá náhodně. Je mu
jedno jak to proběhlo posledně.
""")
input()
print("""
A nyní se podíváme, co se stane když se jednotlivé strategie postaví proti sobě v různém počtu konfliktů.
Poté co se hra zeptá zda chcete spustit serii napište jednodušše ano. Poté máte možnost upravit poměr jednotlivých
strategií v populaci. Celkem musí být zastoupení 100, ale nemusí být použity všechny strategie.
Poté zvolte počet interakcí, které proběhnou. Na konci se dozvíte jak si jednotlivé strategi vedly.
""")




while True:
    answer=input("Chceš spustit sérii? ")
    if answer== "ano" or answer== "ANO" or answer == "Ano":
        kybl1=[]
        kybl2=[]
        celkem=0
        ans=input("Chceš zvolit poměr jednotlivých strategií? Pokud ne, poměr bude 1:1:1:1:1. ")
        if ans== "ano" or ans== "ANO" or ans == "Ano":
            while celkem !=100:
                vloza=int(input("Zastoupení strategie Copycat v % "))
                celkem=celkem+vloza
                print("Ještě zbývá", 100-celkem, "procentních bodů")
                vlozb=int(input("Zastoupení strategie Hustler v % "))
                celkem=celkem+vlozb
                print("Ještě zbývá", 100-celkem, "procentních bodů")
                vlozc=int(input("Zastoupení strategie Jesus v % "))
                celkem=celkem+vlozc
                print("Ještě zbývá", 100-celkem, "procentních bodů")
                vlozd=int(input("Zastoupení strategie IDK v % "))
                celkem=celkem+vlozd
                print("Ještě zbývá", 100-celkem, "procentních bodů")
                vloze=int(input("Zastoupení strategie John Wick v % "))
                celkem=celkem+vloze
                print("Ještě zbývá", 100-celkem, "procentních bodů")
                if celkem !=100:
                    print("Výsledek musí být přesně 100 %, zkus to ještě jednou")
                    celkem=0
                    
            while vloza !=0:
                kybl1.append(a)
                vloza=vloza-1
            while vlozb !=0:
                kybl1.append(b)
                vlozb=vlozb-1
            while vlozc !=0:
                kybl1.append(c)
                vlozc=vlozc-1
            while vlozd !=0:
                kybl1.append(d)
                vlozd=vlozd-1
            while vloze !=0:
                kybl1.append(e)
                vloze=vloze-1
            celkem = 0
           
            while celkem !=100:
                vloza=int(input("Zastoupení strategie Copycat v % ve druhé sadě "))
                celkem=celkem+vloza
                print("Ještě zbývá", 100-celkem, "procentních bodů")
                vlozb=int(input("Zastoupení strategie Hustler v % ve druhé sadě "))
                celkem=celkem+vlozb
                print("Ještě zbývá", 100-celkem, "procentních bodů")
                vlozc=int(input("Zastoupení strategie Jesus v % ve druhé sadě "))
                celkem=celkem+vlozc
                print("Ještě zbývá", 100-celkem, "procentních bodů")
                vlozd=int(input("Zastoupení strategie IDK v % ve druhé sadě "))
                celkem=celkem+vlozd
                print("Ještě zbývá", 100-celkem, "procentních bodů")
                vloze=int(input("Zastoupení strategie John Wick v % ve druhé sadě "))
                celkem=celkem+vloze
                print("Ještě zbývá", 100-celkem, "procentních bodů")
                if celkem !=100:
                    print("Musí se využít přesně 100 %, zkus to ještě jednou")
                    celkem=0
                    
            while vloza !=0:
                kybl2.append(a)
                vloza=vloza-1
            while vlozb !=0:
                kybl2.append(b)
                vlozb=vlozb-1
            while vlozc !=0:
                kybl2.append(c)
                vlozc=vlozc-1
            while vlozd !=0:
                kybl2.append(d)
                vlozd=vlozd-1
            while vloze !=0:
                kybl2.append(e)
                vloze=vloze-1
        else:
            vloza=20
            vlozb=20
            vlozc=20
            vlozd=20
            vloze=20
            while vloza !=0:
                kybl2.append(a)
                kybl1.append(a)
                vloza=vloza-1
            while vlozb !=0:
                kybl2.append(b)
                kybl1.append(b)
                vlozb=vlozb-1
            while vlozc !=0:
                kybl2.append(c)
                kybl1.append(c)
                vlozc=vlozc-1
            while vlozd !=0:
                kybl2.append(d)
                kybl1.append(d)
                vlozd=vlozd-1
            while vloze !=0:
                kybl2.append(e)
                kybl1.append(e)
                vloze=vloze-1
        tlak=input("Jaký má být evoluční tlak. Silný/střední/slabý?")
        press=["Silný","silný","Střední","střední","Slabý","slabý"]
        while tlak not in press:
            print("Nerozumím, zkus to znovu")
            tlak=input("Jaký má být evoluční tlak? Silný/střední/slabý?")
        if tlak == "Silný" or tlak =="silný":
            sila=45
        if tlak =="Střední" or tlak =="střední":
            sila=25
        if tlak=="Slabý" or tlak=="slabý":
            sila=10

        serie=int(input("Počet serií konfliktů "))
        celkem=0
        while celkem != serie:
            pocitadlo=0
            balik1=random.choice(kybl1)
            balik2=random.choice(kybl2)
            karma1=0
            karmaplus1=0
            karma2=0
            karmaplus2=0
            score1=0
            score2=0
            while pocitadlo !=10:
                tah_pc1=(balik1(karma1,karmaplus1))
                tah_pc2=(balik2(karma2,karmaplus2))
                if tah_pc1 == "N" and tah_pc2=="N":
                    karma1=0
                    karma2=0
                    score1=score1+5
                    score2=score2+5
                if tah_pc1=="P" and tah_pc2=="P":
                    karma1=1
                    karma2=1
                if tah_pc1=="N" and tah_pc2=="P":
                    karma1=1
                    karma2=0
                    score2=score2+10
                if tah_pc1=="P" and tah_pc2=="N":
                    karma1=0
                    karma2=1
                    score1=score1+10
          
                karmaplus1=karmaplus1+karma1
                karmaplus2=karmaplus2+karma2
                pocitadlo=pocitadlo+1
                if pocitadlo ==10:
                    if score1 >=sila:
                        kybl1.append(balik1)
                        if len(kybl1) >=101:
                            cislo=randrange(0,100)
                            kybl1.pop(cislo)
                            cislo=0
                    
                    if score2 >=sila:
                        kybl2.append(balik2)
                        if len(kybl2) >=101:
                            cislo=randrange(0,100)
                            kybl2.pop(cislo)
                            cislo=0
                   
                    

                
            celkem=celkem+1
        a1=kybl1.count(a)
        b1=kybl1.count(b)
        c1=kybl1.count(c)
        d1=kybl1.count(d)
        e1=kybl1.count(e)
        print("copycat",a1,"hustler",b1,"jesus",c1,"idk",d1,"johnwick", e1)
        a2=kybl2.count(a)
        b2=kybl2.count(b)
        c2=kybl2.count(c)
        d2=kybl2.count(d)
        e2=kybl2.count(e)
        print("copycat",a2,"hustler",b2,"jesus",c2,"idk",d2,"johnwick", e2)
    else:
        print("Bylo mi potěšením")
        break
        
            



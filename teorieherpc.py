import random
from random import randrange
from coppycac import copycat, hustler, jesus, idk, johnwick
a=copycat
b=hustler
c=jesus
d=idk
e=johnwick
kybl1=[a,b,c,d,e,a,b,c,d,e,a,b,c,d,e,]
kybl2=[a,b,c,d,e,a,b,c,d,e,a,b,c,d,e,]
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
            if score1 >=45:
                kybl1.append(balik1)
                if len(kybl1) >=101:
                    cislo=randrange(0,100)
                    kybl1.pop(cislo)
                    cislo=0
            
            if score2 >=45:
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
    
        


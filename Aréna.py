#Simulátor arény. Nejsou nijak zvláště vyladěné atributy jednotlivých aktivit, zatím jsem se spokojil s tím že to funguje.
from random import randrange, uniform
print ("Aréna")
print ("Simulátor arény - tedy snad")
jmeno = input ("Pojmenuj svého válečníka ")
print ("Vítej", jmeno, "vyber si zaměření.")
print ("Vyber si zaměření")
zaměření = int(input("Gladiator(1), šermíř (2), pěšák (3) "))
if zaměření == 1:
    print ("Jsi gladiátor", jmeno, ", máš větší sílu, ale menší obratnost")
    zdravi = 600
    sance = 1.2
    utok = 30
elif zaměření == 2:
    print ("Jsi šermíř",jmeno,", máš menší sílu, ale větší obratnost")
    zdravi = 200
    sance = 4
    utok = 10
elif zaměření == 3:
    print ("Jsi pěšák",jmeno,", máš vyrovnanou sílu i obratnost")
    zdravi = 300
    sance = 2
    utok = 20
else:
    print ("Nepochopil jsi zadání? Zkus to znovu")
    print ("Vyber si zaměření")
    zaměření = int(input ("Gladiator(1), šermíř (2), pěšák (3) "))
    if zaměření == 1:
        print ("Jsi gladiátor",jmeno,", máš větší sílu, ale menší obratnost")
        zdravi = 600
        sance = 1.2
        utok = 30
    elif zaměření == 2:
        print ("Jsi šermíř",jmeno,", máš menší sílu, ale větší obratnost")
        zdravi = 200
        sance = 4
        utok = 10
    elif zaměření == 3:
        print ("Jsi pěšák",jmeno, ", máš vyrovnanou sílu i obratnost")
        zdravi = 300
        sance = 2
        utok = 20
while zdravi > 0:
    enemy = randrange(0,6)
    if enemy == 0:
        proti="Kazisvět"
    elif enemy == 1:
        proti="Hanz Dobyvatel"
    elif enemy == 2:
        proti="Chropotal"
    elif enemy == 3:
        proti="Hogofogo"
    elif enemy == 4:
        proti="Sauronson"
    elif enemy == 5:
        proti="Badboy"
    input()
    zdravi_proti = 200
    utok_proti = 20
    print("Proti tobě nastupuje protivník", proti)
    while zdravi_proti > 0:
        print("Zvol si způsob boje. Silnější útok má menší šanci na úspěch, ale ubere více zdraví")
        boj = int(input("Úder smrti (1), to nerozchodí, (2) hospodská rvačka (3), šimri šimri (4) "))
        chance = randrange(0,101)
        if boj ==1:
            hit = "Úder smrti"
            sila = 4
        if boj ==2:
            hit ="To nerozchodí"
            sila = 3
        if boj ==3:
            hit ="Hospodská rvačka"
            sila = 2
        if boj ==4:
            hit ="Šimri šimri"
            sila = 1
        
        print("Zaútočil jsi na protivníka", proti,"útokem", hit)
        if boj ==1 and chance <90:
            print("Utok se nezdařil")
        if boj ==1 and chance >=90:
            uder = sila*utok
            zdravi_proti = zdravi_proti - uder
            print ("Útok se podařil! Protivník", proti,"má aktuálně",zdravi_proti,"zdravi." )
            if zdravi_proti <=0:
                print("Porazil jsi", proti," v tomto boji vítězíš!")
                break
        if boj ==2 and chance <65:
            print("Utok se nezdařil")
        if boj ==2 and chance >=65:
            uder = sila*utok
            zdravi_proti = zdravi_proti - uder
            print ("Útok se podařil!Protivník", proti,"má aktuálně",zdravi_proti,"zdravi." )
        if boj ==3 and chance <30:
            print("Utok se nezdařil")
        if boj ==3 and chance >=30:
            uder = sila*utok
            zdravi_proti = zdravi_proti - uder
            print ("Útok se podařil! Protivník", proti,"má aktuálně",zdravi_proti,"zdravi." )
        if boj ==4 and chance <5:
            print("Utok se nezdařil")
        if boj ==4 and chance >=5:
            uder = sila*utok
            zdravi_proti = zdravi_proti - uder
            print ("Útok se podařil! Protivník", proti,"má aktuálně",zdravi_proti,"zdravi." )
        input()
        print ("Protivník",proti,"útočí")
        print ("Zvol si úhybný manévr.")
        print ("Lepším manévrem získáš menší poškození, ale je menší šance na provedení")
        skok = int(input("Mě nedostaneš(1), Ani to nezkoušej (2), Tak si bouchni (3), Dělej si, co chceš (4)"))
        chance = randrange(0,101)
        if skok ==1:
            uf = "Mě nedostaneš"
            slide = 1
        if skok ==2:
            uf ="Ani to nezkoušej"
            slide = 2
        if skok ==3:
            uf ="Tak si bouchni"
            slide = 3
        if skok ==4:
            uf ="Dělej si co chceš"
            slide = 4
        print("Zvolil jsi uhýbný manévr", uf)
        if skok==1 and chance <90:
            print("Úhybný manévr se nezdařil. Dostal jsi",utok_proti,"poškození.")
            zdravi = zdravi - utok_proti
        if skok==1 and chance >=90:
            print("Úhybný manévr se podařil! Neobdržel jsi žádné poškození.")
        if skok==2 and chance <75:
            print("Úhybný manévr se nezdařil. Dostal jsi",utok_proti,"poškození.")
            zdravi = zdravi - utok_proti
        if skok==2 and chance >=75:
            utok2 = utok_proti - 2*sance
            zdravi = zdravi - utok2
            print("Úhybný manévr se podařil! Obdržel jsi pouze",utok2,"poškozeni.")
        if skok==3 and chance <30:
            print("Úhybný manévr se nezdařil. Dostal jsi",utok_proti,"poškození.")
            zdravi = zdravi - utok_proti
        if skok==3 and chance >=30:
            utok2 = utok_proti - 1*sance
            print("Úhybný manévr se podařil! Obdržel jsi pouze",utok2,"poškozeni.")
            zdravi = zdravi - utok2
        if skok==4 and chance <5:
            print("Úhybný manévr se nezdařil. Dostal jsi",utok_proti,"poškození.")
        if skok==4 and chance >=5:
            utok2 = utok_proti - 0.2*sance
            print ("Úhybný manévr se podařil! Obdržel jsi pouze",utok2,"poškození.")
            zdravi = zdravi - utok2
        print("Aktualně máš",zdravi,"zdraví.")
            
            
          
        input()
    
    
    




        

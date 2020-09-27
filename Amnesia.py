from random import randrange
from udalost import amnesia_udalosti

print("Amnesia alfaverze")
sever=0
východ=0
telo=0
obesenec=0



inventar=["vzkaz","klic"]
print("""Vítejte ve textové adventuře Amnesia. Hra se ovládá příkazy napsáním příkazů. Základní příkazy jsou
"jdi na sever","jdi na východ","jdi na jih","jdi na západ", které slouží k pohybu po mapě. Příkaz "inventář" vypíše obsah inventáře.
Příkaz "souřadnice" vypíše současné souřadnice postavy. Příkaz "prozkoumat" vyvolá interanci s objektem
který tuto možnost povoluje. Pro vypsání možných příkazů napiš "příkazy". V ostatních případech hra v závorkách()
nabídne způsob volby. Pro pokračování stiskni Enter""")
input()

print("""Probudil jsi se na mýtině uprostřed lesa. Bolí tě hlava.
Sáhneš na bolavé místo a zjistíš, že krvácíš.
V kapse najdeš kapesník a dočasně s ním ošetříš ránu.
Nepamatuješ si, jak jsi se sem dostal ani kdo jsi.
Na nejbližším stromě najdeš lístek, na který někdo
v rychlosti načmáral vzkaz. Na lístku stojí:
"Najdi mě Tome!" J.""")
input()

while True:
    smer=input("Co uděláš? ")
    if smer == "inventář":
        print(inventar)
    if smer == "příkazy":
        print(""""jdi na sever","jdi na východ","jdi na jih","jdi na západ","inventář","souřadnice","prozkoumat","příkazy" """)
    if smer == "souřadnice":
        print("Sever", sever, "a východ", východ)
    if smer=="jdi na sever":
        sever = sever +1
        if sever == 10:
            print("Odešel by jsi z lesa, ale ještě máš nedořešené nějaké záležitosti")
            sever = sever -1
        
    if smer=="jdi na východ":
        východ = východ + 1
        if východ == 10:
            print("Odešel by jsi z lesa, ale ještě máš nedořešené nějaké záležitosti")
            východ = východ -1
    if smer=="jdi na jih":
        sever = sever + 10
        if sever == -10:
            print("Odešel by jsi z lesa, ale ještě máš nedořešené nějaké záležitosti")
            sever = sever +1
            
    if smer=="jdi na západ":
        východ = východ - 1
        if východ == -10:
            print("Odešel by jsi z lesa, ale ještě máš nedořešené nějaké záležitosti")
            východ = východ + 1
    if sever == 5 and východ ==6:
        print("Stojíš před chatou")
        ans=input("Chceš vstoupit? ")
        if ans == "ano" and "klic" in inventar:
            print("""Odemkl jsi chatu")
Vstoupil jsi do místnosti. Je modernější než by se mohlo zdát podle vzhledu chalupy. Uprostřed místnosti je stůl,
na stole je počítač. Vlevo od tebe jsou dveře. Napravo je skříň. Naproti dveřím je obraz.""")
            ans=input("Co uděláš? (Z)kontrolovat stůl, (PR)ohlédnout počítač, (P)rohledat skříň, (O)tevřít dveře, (PO)dívat se na obraz")
            if ans == "Z":
                print("Přistoupil jsi ke stolu. Na stole jsou fotografie moderního vězeňského zařízení.")
            if ans == "PR":
                print("Sedl jsi si opatrně k počítači. Stále nevíš jestli tě někdo sleduje. Počítač vyžaduje heslo.")
                heslo=input("Zadej heslo: ")
                if heslo !="Sofie":
                    print("Heslo je nesprávné")
                else:
                    print("Fungovalo to! Jsi v systému. Ale co tu vlastně hledáš?")
                      
        if ans =="ano" and "klic" not in inventar:
            print("Chata je zamčená")
            
    if sever == -6 and východ ==0: #STUDNA
        print("Narazil jsi na studnu")
        print(inventar)
        ans=input("Co uděláš? ")
        if ans == "prozkoumat" and "baterka" in inventar:
                print("Studna je hluboká a vyschlá. Na dně vidíš malou skříňku a lesklý předmět")
                ans=input("Co uděláš ")
                if ans=="prozkoumat" or ans=="Prozkoumat" and "lano" in inventar:
                        print("""Uvázal jsi lano k nejbližšímu stromu a začal pomalu slaňovat do studny.Stěny jsou vlhké, porostlé mechem
a dost kloužou. Přesto jsi úspěšně slanil až na dno. Lesklý předmět, který si viděl ze shora je klíč. Ve skříňce
se nachází fotografie a flash disk. Na fotografii se nachází malá holčička se světlými vlasy
a červených šatech s bílými puntíky. Na druhé straně fotografie stojí :" Sofie, 1987" """)
                        ans=input("Chceš umístit předměty do inventáře? ")
                        if ans=="ano" or "Ano":
                            inventar.append("klic")
                            inventar.append("flashka")
                            inventar.append("fotografie")
                            print("Předměty, klíč, flash disk a fotografie byly umístěny do inventáře")
                elif ans=="prozkoumat"  and "lano" not in inventar:
                        print("Nemáš se jak bezpečně dostat dolu a nahoru. Chtělo by to nějaké lano")
        elif ans == "prozkoumat" and "baterka" not in inventar:
                print("Studna je přiliš hluboká, nevidíš, co se nachází na dně. Potřebuješ nějaké světlo.")

    if sever == 3 and východ ==-6 and "páčidlo" not in inventar: #páčidlo
        print(""" Na zemi jsi našel starší páčidlo. Je sice trochu rezavé a poměrně těžké, ale mohlo by se hodit.""")
        ans=input("Přeješ si umístit páčidlo do inventáře? ")
        if ans == "Ano" or "ano":
            inventar.append("páčidlo")
            print("Páčidlo bylo umístěn do inventáře")
    if sever == -4 and východ == 7: #sud
        print("V zemi je polozahrabaný sud")
        ans=input("Co uděláš? ")
        if ans==prozkoumat:
            print("Se sudem nejde pořádně hnout, je pevně zaražený do země. Jeho víko by nicméně šlo nějak (O)tevřít")
            ans2=input("Co uděláš? ")
            if ans2== "O" and "páčidlo" in inventar:
                print("""Vzal jsi páčidlo a po chvíli se ti podařilo víko sundat. Na dně sudu se nachází baterka, pistole a plastová kartička
Po bližším ohledání zjistíš že pistole je vybitá. Na kartičce není žádný text, patrně je uvnitř nějaký čip.""")
                ans3=input("Přeješ si předměty umístit do inventáře? (ano)/(ne)")
                if ans3 == "ano":
                    inventar.append("baterka")
                    inventar.append("pistole")
                    inventar.append("plastová kartička")
            if ans2=="O" and "páčidlo" not in intentar:
                print("Bohužel nemáš nic, čím by to šlo vypáčit")
                    
        

   
    if sever == -3 and východ ==-3 and telo ==0: #tělo
        print("Skoro by jsi to přehlédl. U stromu sedí neznámý člověk.")
        ans=input("Co uděláš? ")
        if ans=="prozkoumat":
            print("""Pomalu jsi se přiblížil k postavě. Jedná se o staršího muže s plnovousem, ve kterém se pomalu objevují šediny. Z dálky to vypadalo
že spí, protože měl bradu položenou na hrudi. Při bližším prozkoumání však zjistíš, že je mrtvý. Někdo mu vrazil do hrudi nůž a vousy ho pak skryly.
Může to být ´J.´ ze vzkazu?""")
            ans=input("Přeješ si muže prohledat? (ano)/(ne)")
            if ans=="ano":
                    print("""Opatrně vsuneš ruku pod kabát a v náprsní kapse objevíš navštívenku Aleš Vybíral, investigativní reportér")
Dobře, "J" to není. Ale co se stalo tomuhle chudákovi? Zjevně tu není bezpečno. Nic jiného jsi u něho neobjevil. Doklady, mobil, nic.""")
            ans2=input("Chceš si vzít nůž? (ano)/(ne) ")
            if ans2 =="ano":
                inventar.append("nůž")
            telo=1
    if sever == -3 and východ ==-3 and telo ==1:
        print("Stojíš před mrtvým Alešem Vybíralem. Je k nevíře, že jsi v první chvíli myslel, že jen spí. Kdo to proboha udělal?")
    if sever ==-7 and východ == 7:
        if telo == 1:
            print("Proboha! Další mrtvola! Tentokrát je to oběšenec. Pomohl mu někdo nebo je to jen shoda okolností?")
        if telo == 0:
            print("Z dálky jsi to úplně nepoznal, ale nyní vidíš, že z větve u blízkého stromu visí oběšenec. Tento les je čím dál více děsivý")
        ans=input("Co uděláš? ")
        if ans=="prozkoumat":
            print("""Při bližším ohledání zjistíš, že jde o dobře oblečeného mladíka. Proč by šel do hlubokého lesa, aby se oběsil? Nikde není žádné zavazadlo,
které by přinesl s sebou. Jeden konec lana je uvázaný kolem kmenu stromu, druhý přehozen přes silnou větev a pod ní visí na smyčce zmíněný mladík.""")
            ans2== input("Přeješ si oběšence odvázat? (ano)/(ne) ")
            if ans2 == ano and "nůž" in inventar:
                print("""Provaz je přiliš napnutý, na to aby šel odvázat. Máš u sebe však nůž, kterým šel provaz přeříznout. Opatrně spouštíš mladíka na zem. Nemá
u sebe nic. co by mohlo být jakýmkoliv způsobem užitečné. """)
                ans3=input ("Chceš si vzít provaz? (ano)/(ne)" )
                if ans3== "ano":
                    print("""Dalo ti to sice dost práce, aby jsi provaz sundal, ale nakonec se ti to podařilo. Mladík se pravděpodobně nezabil sám, ale
ani jsi na něm neobjevil stopy po násilí. Přesunul jsi mladíka ke stromu, smotal lano a pokračuješ v cestě.""")
                    inventar.append("lano")
                    obesenec=1
            if ans2 == ano and "nůž" not in inventar:
                print("""Provaz je příliš napnutý, aby jsi ho mohl snadno rozvázat. Potřebuješ něco, čím provaz přeřízneš""")
                
    if sever == -7 and východ ==7 and obesenec ==1:
        print("Stojíš u stromu, kde jsi nechal ležet mladíka. Nemůžeš mu nijak pomoci. Je smutné, že zemřel tak mladý")
            
                  
            

    if sever == -8 and východ == -8:
        print(""" Narazil jsi na ceduli "Nacházíte se ve vojenském prostoru. Neprodleně opusťte tuto oblast!!!" Kde to k sakru ,jsi?! """)
    if sever == 8 and východ == 8:
        print(""" Narazil jsi na ceduli "Nacházíte se ve vojenském prostoru. Neprodleně opusťte tuto oblast!!!" Kde to k sakru ,jsi?! """)

    

                
                                  
    if sever == 10 or východ == 10 or sever == -10 or východ == -10:
        print("Odešel by jsi z lesa, ale ještě máš nedořešené nějaké záležitosti")
    
    
    else:
            print("Jsi v lese")
    udalost()

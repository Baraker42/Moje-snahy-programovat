#Textová adventura. Je ve velmi rané fázi. Nemá v tuto chvíli žádný endgame
sever=0
východ=0
inventar=["vzkaz"]

print("Probudil jsi se na mýtině uprostřed lesa. Bolí tě hlava.")
print("Sáhneš na bolavé místo a zjistíš, že krvácíš.")
print("V kapse najdeš kapesník a dočasně s ním ošetříš ránu.")
print("Nepamatuješ si, jak jsi se sem dostal ani kdo jsi.")
print("Na nejbližším stromě najdeš lístek, na který někdo")
print("v rychlosti načmáral vzkaz. Na lístku stojí:")
print("Najdi mě Tome! J.")
input()

while True:
    smer=input("Kam půjdeš? ")
    if smer == "inventář":
        print(inventar)
    if smer == "souradnice":
        print("Sever", sever, "a východ", východ)
    if smer=="sever":
        sever = sever +1   
    if smer=="východ":
        východ = východ + 1     
    if smer=="jih":
        sever = sever - 1 
    if smer=="západ":
        východ = východ - 1
    if sever == 2 and východ == 2:
        print("stojíš před chalupou")
        ans=input("Chceš vstoupit? ")
        if ans == "ano" and "klic" in inventar:#vždy je potřeba specifikovat podmínky
            # u všech podmínke musí být specifikované čeho se týkají
            print("odemkl jsi chalupu")
            print("Vstoupil jsi do místnosti. Je modernější než by se mohlo zdát podle vzhledu chalupy.")
            print("uprostřed místnosti je stůl, na stole je počítač. Vlevo od tebe jsou dveře. Napravo je skříň.")
            ans=input("Co uděláš? (Z)kontrolovat stůl, (PR)ohlédnout počítač, (P)rohledat skříň, (O)tevřít dveře")
        if ans =="ano" and "klic" not in inventar:
            print("chalupa je zamčená")
            
    if sever == 5 and východ ==1: #STUDNA
        print("Narazil jsi na studnu")
        print(inventar)
        ans=input("Co uděláš? ")
        if ans == "prozkoumat" and "baterka" in inventar:
                print("Studna je hluboká a vyschlá. Na dně vidíš malou skříňku a lesklý předmět")
                ans=input("Co uděláš? ")
                if ans=="prozkoumat" or ans=="Prozkoumat" and "lano" in inventar:
                        print("Uvázal jsi lano k nejbližšímu stromu a začal pomalu slaňovat do studny.")
                        print("Stěny jsou vlhké, porostlé mechem a dost kloužou. Přesto jsi úspěšně")
                        print("slanil až na dno. Lesklý předmět, který si viděl ze shora je klíč. Ve skříňce se")
                        print("nachází fotografie a flash disk. Na fotografii se nachází malá holčička se světlými vlasy")
                        print("a červených šatech s bílými puntíky. Na druhé straně fotografie stojí")
                        print("Sofie, 1987")
                        ans=input("Chceš umístit předměty do inventáře? ")
                        if ans=="ano" or "Ano":
                            inventar.append("klic")
                            inventar.append("flashka")
                            inventar.append("fotografie")
                            print("Předměty, klic, flash disk a fotografie byly umístěny do inventáře")
                elif ans=="prozkoumat"  and "lano" not in inventar:
                        print("Nemáš se jak bezpečně dostat dolu a nahoru. Chtělo by to nějaké lano")
        elif ans == "prozkoumat" and "baterka" not in inventar:
                print("Studna je přiliš hluboká, nevidíš, co se nachází na dně. Potřebuješ nějaké světlo.")

    if sever == -3 and východ ==6: #klacek
        print("Na zemi před tebou leží kus dřeva")
        print("Při bližším ohledání zjistíš, že je poměrně pevné")
        print("a mohlo by sloužit jako provizorní zbraň")
        ans=input("Přeješ si umístit klacek do inventáře? ")
        if ans == "Ano" or "ano":
            inventar.append("klacek")
            print("Klacek byl umístěn do inventáře")

   
    if sever == 4 and východ ==2:
        print("Skoro by jsi to přehlédl. U stromu sedí neznámý člověk")
        print("Pokud chceš zjistit o koho se jedná napiš(prověřit)")
        print("v opačném případě napiš jakýkoliv jiný příkaz")
        ans=input("Co uděláš? ")
        if ans=="prověřit":
            print("Pomalu jsi se přiblížil k postavě. Jedná se o staršího muže")
            print("s plnovousem, ve kterém se pomalu objevují šediny.Z dálky to vypadalo")
            print("že spí, protože měl bradu položenou na hrudi. Při bližším prozkoumání")
            print("však zjistíš, že je mrtvý. Někdo mu vrazil do hrudi nůž a vousy ho pak skryly.")
            print("Může to být ´J.´ ze vzkazu?")
            ans=input("Přeješ si muže prohledat? ano/ne")
                if ans=="ano":
                    print("Opatrně vsuneš ruku pod kabát a v náprsní kapse objevíš navštívenku")
                    print("Aleš Vybíral, .....")
                    print("Dobře, ´J´to není. Ale co se stalo tomuhle chudákovi? Zjevně tu není bezpečno. ")
                    print("Nic jiného jsi u něho neobjevil. Doklady, mobil, nic."
            ans2=input("Chceš si vzít nůž? ano/ne ")  
                       

                
                                  
    if sever == 15 or východ == 15 or sever == -15 or východ == -15:
        print("Odešel by jsi z lesa, ale ještě máš nedořešené nějaké záležitosti")
    else:
            print("Jsi v lese")

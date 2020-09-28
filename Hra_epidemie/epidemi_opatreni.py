def opatreni(izolace,testovani,prevence):
    #print("Rozpočet",rozpocet)
    
    #print("Počet zemřelých", zemrely")
    while True:
        print("Jaké změny si přejete provést, případně jaké informace si přejete prohlédnout?")
        volba=input("Co si přejte upravit? ")
        if volba == "Testování":
            zmena=input("Jak si přejte upravit financování testování? Zvolte zvýšit/snížit")
            if zmena == "zvýšit":
                kolik=int(input("O kolik?"))
                testovani=testovani+kolik
            if zmena == "snížit":
                kolik=int(input("O kolik?"))
                testovani=testovani-kolik
        if volba == "Izolace":
            zmena=input("Přejete si dát do karanteny všechny pozitivně testované?")
            if zmena == "ANO":
                izolace=True              
        if volba =="Konec":
            break
        if volba == "Prevence":
            zmena = input("Přejete si zavést povinné roušky/respirátory")
            prevence.append(zmena)
        
        print(izolace)
    return(izolace,testovani,prevence)
        

from random import randrange, uniform
print ("Ruleta")
peníze = 500
while peníze >= 0:
    volba = input("Chceš vsadit na ČÍSLO nebo BARVU? ")
    if volba == "ČÍSLO":
        cislo = int(input("Napiš číslo, na které chceš vsadit "))
        sázka = int(input("Napiš kolik chceš vsadit "))
        if sázka > peníze:
            print("Na koho to zkoušíš mladej")
            break
        ruleta = randrange(0,37)
        print ("Vyhrává číslo", ruleta)
        input()
        if ruleta == cislo:
            print ("Vyhráváš!")
            peníze = peníze + sázka*10
        elif ruleta != cislo:
            print ("Ty prohráváš")
            peníze = peníze - sázka
        print ("Aktuálně máš", peníze)
        input()
    
    if volba == "BARVU":
        colour = input("A bude to ČERVENÁ nebo ČERNÁ? ")
        sázka = int(input("Napiš kolik chceš vsadit "))
        if sázka > peníze:
            print("Na koho to zkoušíš mladej")
            break
        ruleta = randrange(0,37)
        if ruleta % 2 == 0:
            barva = "ČERVENÁ"
            print("Číslo je červené.")
        else:
            barva = "ČERNÁ"
            print("Číslo je černé.")
        input()
        if barva == colour:
                    print ("Vyhráváš!")
                    peníze = peníze + sázka*2
        elif barva != colour:
                    print("Ty prohráváš")
                    peníze = peníze - sázka
        print ("Aktuálně máš", peníze)
        input()
else:
        print("Přečti si zadání a zkus to znovu")
    

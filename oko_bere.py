from random import randrange
body = 0
while body <21:
    print ("Aktuálně máš", body, "bodů")
    odpoved = input ("Přeješ si další kartu? ano/ne ")
    if odpoved =="ano":
            hodnota = randrange (2,11) #je třeba aby bylo poslední číslo o jednu hodnotu větší
            body = body + hodnota
            if body > 21:
                print("Máš přesně", body, "bodů. To už je moc, prohráváš")
            if body == 21:
                print("Vyhráváš zlatého bludišťáka")
    if odpoved == "ne":
        print ("Skončil jsi s", body, "chybělo ti", 21-body, "do plného počtu")
        break
        

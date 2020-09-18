print ("Pokladna 0.3 - Alfa verze")
pokladna = int(input("Kolik je na začátku dne v pokladně? "))
pokladna1=pokladna

celkova_cena=0
pocet_zakazniku=0
den="Další"
while den =="Další":
    while True:
        try:
            cena=int(input("Vlož cenu produktu. "))
            celkova_cena = celkova_cena + cena
        except ValueError:
            break
    print("Nákup stojí", celkova_cena)
    try:
        
        platba = int(input("Zákazník platí "))
    except ValueError:
        print("Byla zadána neplatná hodnota")
        platba = int(input("Zákazník platí "))
    vratit=platba-celkova_cena
    print("Vraťte zákazníkovi", vratit)
    input()
    pokladna = pokladna+(platba-vratit)
    print("Aktuální stav pokladny:"pokladna)
    pocet_zakazniku=pocet_zakazniku + 1
    celkova_cena=0
    den = input("Další/Konec ")
print("Celkový počet zákazníků za dnešek je", pocet_zakazniku)
print("V pokladně se momentálně nachází", pokladna)
prumer=(pokladna-pokladna1)/pocet_zakazniku
print("Zákazník průmerně utratil",prumer,"za jeden nákup")
    

input()
               

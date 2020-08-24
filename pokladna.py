#Jeden z prvních vytvořených programů. Sčítá jednotlivé položky, řekne konečnou cenu, zeptá se na hodnotu, kterou platí zákazník a vypíše návratovou sumu.
#nakonci dne zhodnotí obsah pokladny a vypíše průměrnou útratu za jeden nákup.
print ("Pokladna 0.1 - Alfa verze")
pokladna = int(input("Kolik je na začátku dne v pokladně? "))
pokladna1=pokladna
cena=""
celkova_cena=0
pocet_zakazniku=0
den="Další"
while den =="Další":
    while cena !=0:
        cena=int(input("Vlož cenu produktu. "))#pokud není žádný další produkt třeba napsat "0"
        celkova_cena = celkova_cena + cena
    print("Nákup stojí", celkova_cena)
    platba = int(input("Zákazník platí "))
    vratit=platba-celkova_cena
    print("Vraťte zákazníkovi", vratit)
    input()
    pokladna = pokladna+(platba-vratit)
    print(pokladna)
    pocet_zakazniku=pocet_zakazniku + 1
    celkova_cena=0
    cena=""
    print(cena)
    den = input("Další/Konec ")
print("Celkový počet zákazníků za dnešek je", pocet_zakazniku)
print("V pokladně se momentálně nachází", pokladna)
prumer=(pokladna-pokladna1)/pocet_zakazniku
print("Zákazník průmerně utratil",prumer,"za jeden nákup")
    

input()
               

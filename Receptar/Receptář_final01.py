import json
from receptar_funkce import nahled_receptu, novy_recept, uprava_surovin, vareni
print(""""Receptář alfa verze. Umožňuje evidenci surovin a receptů. Pro náhled již existujících receptů napiš 1.
Pro založení nového receptu napiš 2. Pro úpravu stavu surovin napiš 3. Pro vaření podle receptu napiš 4.""")
konec = "ne"
while konec == "ne":
    volba=int(input("Zvol akci"))
    if volba == 1:
        nahled_receptu()
    if volba ==2:
        novy_recept()
    if volba == 3:
        uprava_surovin()
    if volba == 4:
        vareni()
    konec = input("""Přeješ si provádět nějaká další změny? Pokud ne napiš "ne" a stiskni enter""")

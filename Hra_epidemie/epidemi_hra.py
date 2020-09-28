from epidemie_prubeh import zalozeni, den
from epidemi_opatreni import opatreni
startovaci_rozpocet=10000
denni_prijem=1000
cena_opatrenich=0
dezinformace=0
informace=0
vakcina=0
zdravotnictví=50
testovani=0
nespokojenost=0
prevence=[]
kolaps=5
izolace=False

cislo=int(input("Napiš číslo" ))
set_1=zalozeni(cislo)
while True:
    pastika=den(set_1,testovani,izolace,prevence,kolaps) #spustí funkci "den" na spočítání nových stavů občanů
    nakazeni=[]
    zemrely=[]
    kolaps=pastika[1]
    print(pastika)
    for i in set_1: #vytvoří bilaci za posledni den
        nakazen=i["testovany"]
        zemrel=i["status"]
        nakazeni.append(nakazen)
        zemrely.append(zemrel)
    ano=nakazeni.count(True)
    pocet_zemrelych=zemrely.count("Mrtvý")
    print("Počet pozitivně testovaných", ano)
    print("Počet zemřelých",pocet_zemrelych)
    vysledek=opatreni(izolace,testovani,prevence) #Spustí funkci opatreni - funguje jako maznažerské rozhraní, kde se udávají příkazy
    izolace=vysledek[0]
    testovani=vysledek[1]
    prevence=vysledek[2]
    

#distribuce roušek nebo respirátoru je dlouhodobě dražší než informovat lidi o
    #vhodnosti nošení roušek/respiratorů
#povinné nošení roušek zvyšuje dezinformaci, vyšší informovanost vede k nošení roušek
#zavírání jednotlivých složek vede k nižšímu šíření viru, ale také k nespokojenosti
#hra končí, když jsou všichni vyléčení, vynález a distribuce vakcíny není povinná ani neovlivní score
    #score se spočítá z délky trvání epidemie, financí vyložených na poražení epidemie, zemřelých a nespokojenosti
    #body navíc jde získat vývojem vakcíny a vyšší informovaností

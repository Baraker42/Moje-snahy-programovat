#Tento skript vezme sadu čísel a roztřídí je na prvočísla a na neprvočísla.
sada=[]
ostatni=[]
prvocisla=[]
while True:
    try:
        num=int(input("vlož číslo "))
        sada.append(num)
    except:
        ValueError
        break
print(sada)
delka=len(sada)
delka=delka-1
odpocet=0

while odpocet <=delka:
    cislo=sada[odpocet]
    delitel=1
    poz=0
    
    while delitel <= cislo:
        if cislo % 2 ==0:
           ostatni.append(cislo)
           odpocet=odpocet+1
           
           break
            
        if cislo % delitel==0:
            poz=poz+1
            
        if delitel==cislo and poz<=2:
            odpocet=odpocet+1
            prvocisla.append(cislo)
            break
              
        if poz>=3:
            ostatni.append(cislo)
            odpocet=odpocet+1
            break
        delitel=delitel+1
       
       
          


print("Neprvočísla", ostatni)
print("Prvočísla", prvocisla)


                    
    

from random import randrange, uniform
print ("Mendelovská genetika")
genotyp1 = input ("Zadej genotyp 1 rodiče AA, Aa nebo aa ")
genotyp2 = input ("Zadejte genotyp 2 rodiče AA, Aa nebo aa ")
potomci = int(input("Zadejte počet potomků "))
AA=0
Aa=0
aa=0
genotyp = genotyp1, genotyp2
print(genotyp)
if ("AA" in genotyp1 and "AA" in genotyp2):
    AA = potomci
     
    
elif ("aa" in genotyp1 and "aa" in genotyp2):
    aa = potomci
  
elif ("AA" in genotyp and "aa" in genotyp):
    Aa = potomci

elif "Aa" in genotyp1 and "Aa" in genotyp2:  
    while potomci >=1:
        sance=randrange(0,101)
        if sance <=25:
            AA += 1
        elif sance >25 and sance <75:
            Aa +=1
        elif sance >=75:
            aa +=1
        potomci = potomci - 1

elif "AA" in genotyp and "Aa" in genotyp:
    while potomci >=1:
        sance=randrange(0,2)
        
        if sance ==0:
            AA+=1
        elif sance ==1:
            Aa+=1
        potomci = potomci -1
       

elif "aa" in genotyp and "Aa" in genotyp:
    while potomci >=1:
        sance=randrange(0,2)
        if sance ==0:
            aa+=1
        elif sance ==1:
            Aa+=1
        potomci = potomci -1
        
        
        
print("Genotyp AA zastopen",AA, "potomky")
print("Genotyp Aa zastoupen", Aa, "potomky")
print("Genotyp aa zastoupen", aa, "potomky")
vsichni=AA+Aa+aa
print(vsichni)
AA1=0
Aa1=0
aa1=0
while True:
    AA1=0
    Aa1=0
    aa1=0
    odpoved=input("Přejete si spustit, další generaci ?")
    potomci=int(input("Kolik bude mít každý pár potomků ?"))
    potomci1=potomci
    potomciAa=potomci1
    potomciaa=potomci1
    potomciAA=potomci1
    if odpoved == "ne" or odpoved =="NE" or odpoved == "Ne":
        break
    while vsichni >= 0 or vsichni ==1:
            
            if AA >=2:
                AA1=AA1+potomci
                AA=AA-2
                vsichni=vsichni-2
               
            if aa >=2:
                aa1=aa1+potomci
                aa=aa-2
                vsichni=vsichni-2
                
            if Aa >=2:
                while potomciAa !=0:
                    sance=randrange(0,101)
                    if sance <=25:
                        AA1 += 1
                    elif sance >25 and sance <75:
                        Aa1 +=1
                    elif sance >=75:
                        aa1 +=1
                    potomciAa = potomciAa-1
                Aa=Aa-2
                vsichni=vsichni-2
                
            if Aa >=1 and aa >=1:
                while potomciaa !=0:
                    sance=randrange(0,2)
                    if sance ==0:
                        aa1+=1
                    elif sance ==1:
                        Aa1+=1
                    potomciaa = potomciaa-1
                Aa=Aa-1
                aa=aa-1
                vsichni=vsichni-2
               
            if Aa >=1 and AA>=1:
                while potomciAA !=0:
                    
                    sance=randrange(0,2)
                    if sance ==0:
                        AA1+=1
                    elif sance ==1:
                        Aa1+=1
                   
                    potomciAA = potomciAA-1
                Aa=Aa-1
                AA=AA-1
                vsichni=vsichni-2
                
            if AA >=1 and aa>=1:
                Aa1=Aa1+potomci
                AA = AA-1
                aa = aa -1
                vsichni=vsichni-2
            if vsichni ==0 or vsichni ==1:
                break
            potomciAa=potomci1
            potomciaa=potomci1
            potomciAA=potomci1
            
    
    vsichni = AA1+aa1+Aa1
    AA=AA1
    aa=aa1
    Aa=Aa1
    potomci=0
    potomciaa=0
    potomciAa=0
    potomci1=0
    potomciAA=0
    
    
    
    print("V další generaci je ",AA1, "jedinců s genotypem AA.")
    print("V další generaci je ",aa1, "jedinců s genotypem aa.")
    print("V další generaci je ",Aa1, "jedinců s genotypem Aa.")
    
        
    


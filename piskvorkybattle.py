from random import randrange, uniform
retezec=("--------------------")
cislo=0
vyhra=0
tah=0
print(retezec)
while "-" in retezec and "ooo" not in retezec and "xxx" not in retezec:
    
        
    ans1=int(input("Zadej pozici "))
    ans1=ans1-1
    while "x"in retezec[ans1] or "o" in retezec[ans1]: 
        print("To nejde")
        ans1=int(input("Zadej pozici znovu "))
            
    ans2=ans1+1
    retezec=retezec[:ans1]+"x"+retezec[ans2:]
    ans1=0
    print(retezec)
    if "xxx" in retezec:
        print ("X vyhrává" )
        break
    print(cislo)
    tah=0
    cislo=-1
    
    while cislo != 19 and "ooo" not in retezec:
        print(tah)
        print("číslo",cislo)
        
        if "o" not in retezec:
            
            
            cislo=randrange(0,21)
            if retezec[cislo] =="x":
                cislo=randrange(0,21)
            
            pozice1=retezec[:cislo]
            cislo=cislo+1
            pozice2=retezec[cislo:]
            retezec=pozice1+"o"+pozice2
            
            cislo=0
            
            break
        if retezec[cislo] =="o" and tah==0:
            
            ncislo=cislo+1
            if retezec [ncislo] == "o" or retezec [ncislo]=="x":
                
                ncislo=ncislo+1
                if retezec [ncislo] == "o" or retezec [ncislo]=="x":
                    
                    if retezec [ncislo] =="x" or retezec [ncislo]=="o":
                        cislo=randrange(0,21)
                    
                    
                    pozice1=retezec[:cislo]
                    cislo=cislo+1
                    pozice2=retezec[cislo:]
                    retezec=pozice1+"o"+pozice2
                    
                    cislo=0
                    
                    break
                pozice1=retezec[:ncislo]
                cislo=ncislo+1
                pozice2=retezec[cislo:]
                retezec=pozice1+"o"+pozice2
                
                cislo=0
                tah=1
                

                
            pozice1=retezec[:ncislo]
            cislo=ncislo+1
            pozice2=retezec[cislo:]
            retezec=pozice1+"o"+pozice2
            print(retezec)
            cislo=0
            tah=1
        
        cislo=cislo+1
        if "ooo" in retezec:
            print("O vyhrává")
            vyhra=vyhra+1
       
    
     

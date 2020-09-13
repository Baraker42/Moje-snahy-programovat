#Hra Kámen, Nůžky, Papír obohacená o rozšíření ze seriálu TBBT.
from random import randrange
print("Kámen, nůžky, papír, ještěr, Spock")
score=0
stare_score=0
remiza=1
print("Napíš první písmeno znaku, který volíš")
while True:
        volba=input("(K)ámen, (N)ůžky, (P)apír,(J)eštěr,(S)pock ")
        if volba=="K":
            volba=("Kámen")
        elif volba=="N":
            volba=("Nůžky")
        elif volba=="P":
            volba=("Papír")
        elif volba=="J":
            volba=("Ještěr")
        elif volba=="S":
            volba=("Spock")
        else:
            print("Přečti si znovu zadání")
            
        pc_volba=randrange (1,6)
        
        if pc_volba==1:
            pc_volba=("Kámen")
        if pc_volba==2:
            pc_volba=("Nůžky")
        if pc_volba==3:
            pc_volba=("Papír")
        if pc_volba==4:
            pc_volba=("Ještěr")
        if pc_volba==5:
            pc_volba=("Spock")

        výsledek = pc_volba, volba #pokud chci zajistit že budou platit oba příkazy
        #musím u obou zadat odkud vychází
        if "Kámen" in výsledek and "Spock" in výsledek:
            print("Spock vypaří kámen")
            if volba == ("Spock"):
                    score=score+1
                   
        elif "Kámen" in výsledek and "Nůžky" in výsledek:
            print("Kámen tupí nůžky")
            if volba == ("Kámen"):
                    score=score+1
                  
        elif "Kámen" in výsledek and "Papír" in výsledek:
            print("Papír balí kámen")
            if volba == ("Papír"):
                    score=score+1
                    
        elif "Kámen" in výsledek and "Ještěr" in výsledek:
            print("Kámen drtí ještěra")
            if volba == ("Kámen"):
                    score=score+1
                    
      
            
        elif  "Papír" in výsledek and "Nůžky" in výsledek:
            print("Nůžky stříhají papír")
            if volba == ("Nůžky"):
                    score=score+1
                    
        elif  "Papír" in výsledek and "Spock" in výsledek:
            print("Papír usvědčí Spoka")
            if volba == ("Papír"):
                    score=score+1
                    
        elif  "Papír" in výsledek and "Ještěr" in výsledek:
            print("Ještěr sežere papír")
            if volba == ("Ještěr"):
                    score=score+1
        
                    
       
            
        elif "Nůžky" in výsledek and "Ještěr" in výsledek:
            print("Nůžky přestřihnou ještěra")
            if volba == ("Nůžky"):
                score=score+1
       
                
        elif  "Nůžky" in výsledek and "Spock" in výsledek:
                print("Spock zničí nůžky")
                if volba == ("Spock"):
                    score=score+1
                    
        
                
        elif  "Ještěr" in výsledek and "Spock" in výsledek:
                print("Ještěr otráví Spocka")
                if volba == ("Ještěr"):
                    score=score+1
                    
        else:
             
             remiza=0
      
        
        print("Počítač zvolil", pc_volba, "a ty jsi zvolil", volba)
        if remiza==1:
                if stare_score < score:
                    print("Vyhráváš! Tvoje Aktuální skóre je", score)
                elif stare_score == score:
                    print("Bohužel prohráváš. Ale nezoufej, může to vyjít příště. Tvoje skóre je",score)
        if remiza == 0:
                print("Je to remíza. Nevyhráváš ale ani neprohráváš")
        print("")
        stare_score=score
        remiza=1
        
        
        
       
       
        


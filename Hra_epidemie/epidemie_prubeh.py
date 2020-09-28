#Tento skript bude sloužit k založení setu osob a vyhodnocování dní epidemie.
from random import randrange
def zalozeni (cislo):
    set_1=[]
    
    for i in range (1,cislo): #vytvoří startovací balíček osob
        jedinec={}
        jedinec["osoba"]=i
        set_1.append(jedinec)
        sance=randrange(0,100)
        if sance <30: #určí jestli je jedinec nakažený
            jedinec["Nakažený"]=True
            jedinec["Zbyv.delka.nem"]=20
        else:
            jedinec["Nakažený"]=False
            jedinec["Zbyv.delka.nem"]=0
        jedinec["testovany"]=False
        jedinec["imunita"]=False
        jedinec["zbývá imunity"]=0
        jedinec["rouška"]="NE"
        jedinec["status"]="Živý"
        jedinec["stav"]="OK"
        jedinec["karantena"]=False
    return(set_1)
        

    


def den (set_1,testovani,izolace):
    while True:
        zdravotnictvi=500        
        riziko=100    
        delka=len(set_1)
        celkem=0
        izolace=izolace
        opatreni=""
       
        
        while delka > celkem: #vybere každou osobu ze setu
            osoba=set_1[celkem]
            status=osoba["status"]
            clovek=osoba["osoba"]
            nakazeny=osoba["Nakažený"]
            nemoc=osoba["Zbyv.delka.nem"]
            stav=osoba["stav"]
            testovany=osoba["testovany"]
            karantena=osoba["karantena"]
            sance_odhaleni=randrange(0,100)
            mira_testovani=testovani
            if testovany == False and sance_odhaleni < mira_testovani and nakazeny == True and karantena==False:
               novy_test={"testovany":True}
               osoba.update(novy_test)
               if izolace == True:
                   update_karanteny={"karantena":True}
                   
              
            if opatreni == "roušky":
                rouska=osoba["rouška"]
                rousky_vsem={"rouška":"respirator"}
                osoba.update(rousky_vsem)
            rouska=osoba["rouška"]
            imunni=osoba["imunita"]
            celkem1=celkem+1
            nakaza="ne"
            nova_delka=delka
            imunita_jedince=osoba["zbývá imunity"]
            #testovani čím víc intenzivní testování tak větší šance že dojde k odhalení
            #niméně je nákladnější a zvyšuje dezinformace
            if imunita_jedince >0:
                imunita_jedince=imunita_jedince-1

                if imunita_jedince==0:
                    zbyva_imunity={"zbývá imunity":0,"imunita":False}
                zbyva_imunity={"zbývá imunity":imunita_jedince}
                osoba.update(zbyva_imunity)
            for i in set_1[celkem1:delka]: #tato část skriptu zajistí, že každá osoba se během jednoho dne potká s každou osobou
                riziko=100
                nakazeny_novy=i["Nakažený"]
                ochrana_novy=i["rouška"]
                status=i["status"]
                karantena=i["karantena"]
          
                if ochrana_novy == "rouška":
                    riziko=riziko-10
                elif ochrana_novy =="respirator":
                    riziko=riziko-20
                sance=randrange(0,riziko)   
                if imunni == True or status=="Mrtvý" or karantena == True:
                    sance=0
                sance_setkani=randrange(0,100)
                if sance_setkani >=80:
                    break
                if nakazeny_novy == True and sance >=60:
                    if nakazeny == False:
                        novy={"Nakažený":True,"Zbyv.delka.nem":20}
                        osoba.update(novy)
     
                     
                if nakazeny == True and sance >=80 and nakazeny_novy == False:
                    osoba_nova=i["osoba"]
                    nova={"Nakažený":True,"Zbyv.delka.nem":20}
                    i.update(nova)
                    
            
            if nakazeny==True:
                zhorseni=randrange(0,100)
                if zhorseni<5:
                    novy_stav={"stav":"Vážný","karantena":True,"odhalený":True}
                    zdravotnictvi=zdravotnictvi-1
                    
                    osoba.update(novy_stav)
            if stav == "Vážný":
                zhorseni=randrange(0,100)
                if zhorseni<5:
                    zemrel={"status":"Mrtvý"}
                    osoba.update(zemrel)
                    
                    zdravotnictvi=zdravotnictvi+1
                if zhorseni>80:
                    zlepseni={"stav":"OK"}
                    osoba.update(zlepseni)
          
            
            

               
            if nemoc !=0: #odečítá dny zbývající do konce nemoci
                nemoc=nemoc-1
                if nemoc==0:
                   do_konce={"Nakažený":False,"Zbyv.delka.nem":0,"imunita":True,"zbývá imunity":60,"karantena":False}
                else:
                    do_konce={"Zbyv.delka.nem":nemoc}
                osoba.update(do_konce)
            #print(osoba)
            celkem=celkem+1
            
                  
                    
                    

            
        
        
       
        
        celkem=0
        return(set_1)


        







            
        
        


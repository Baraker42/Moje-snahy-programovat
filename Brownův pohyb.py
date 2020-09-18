from random import randrange, uniform
print("Brownův pohyb")
try:
        cil=int(input("Jak daleko je Brownův maják? "))

        try:
                molo =int(input("Jak široké je molo? "))
        
        

                pozice=0
                strana=0
                while pozice !=cil and strana !=molo and strana !=-molo:
                        pozice +=1
                        zmena=randrange(0,2)
                        if zmena ==0:
                            strana +=1
                        if zmena ==1:
                            strana +=-1
                        print(strana)
                        if strana == molo or strana == -molo:
                            print("Opilý Brown spadl do moře")

                if pozice == cil:
                    print ("Opilý Brown dospěl do majáku, kde se mohl vyspat")
                if pozice != cil:
                    print ("Opilý Brown dnes spí s rybami")
                print("Opilý Brown dospěl do pozice", pozice)
                input()
        except ValueError:
                print("Neplatná hodnota")
            
except ValueError:
        print("Neplatná hodnota")

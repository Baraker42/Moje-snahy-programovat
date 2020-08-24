from random import randrange, uniform
print("Brownův pohyb")
cil=int(input("Jak daleko je Brownův maják? "))
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
    

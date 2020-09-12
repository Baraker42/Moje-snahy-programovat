import json
with open ("soupis_SPZ.json") as f:
    SPZ = json.load(f)

delka=len(SPZ)
celek=0
pokuty=[]
while celek < delka:
    pokuta={}
    spztky=SPZ[celek]
    spz=spztky["SPZ"]
    speed=spztky["Rychlost"]
    if speed > 50:
        pokuta["SPZ"]=spz
        rychlost=str(speed)
        speed_v_km=(rychlost + " km/h")
        pokuta["Rychlost"]=speed_v_km
        pokuty.append(pokuta)
    celek=celek+1
print(pokuty)

with open ("././/nadlimit.json","w") as f:
    json.dump(pokuty, f)

            
                      

#Náhledy receptů - co je potřeba na konkrétní recept
import json
with open ("recepty.json") as f:
           data = json.load(f)
receptar=[]
for i in data:
    
    receptar.append(i)
print(receptar)

while True:
    nahled=input("Který recept si chceš prohlédnout? ")
    try:
        view=data[nahled]
        print(view)
        break
    except KeyError:
        print("Takový recept tu nemám, zkus to ještě jednou")

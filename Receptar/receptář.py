import json


recepty={}
rajcatovka={}
rajcatovka["testoviny"]=500
rajcatovka["konzerva rajcat"]=1

recepty["Rajcatovka"]=rajcatovka


with open ("././/recepty.json", "w") as file:
    json.dump(recepty, file)





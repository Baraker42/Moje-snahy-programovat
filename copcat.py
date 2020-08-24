#Základ většího projektu na základě Teorie her. Zatím pouze verze, která opakuje předchozí hráčův krok.
print("copyCat")
score=0
score_pc=0
pocitadlo=0
karma=1
tah_pc=("N")
while pocitadlo !=10:
    ans=input("(P)odvést/(N)epodvést" )
    if karma==1:
        tah_pc="N"
    if karma==0:
        tah_pc="P"
    if ans == "P" and tah_pc=="N":
        score=score+10
        karma=0
    if ans == "N" and tah_pc=="N":
        score=score+5
        score_pc=score_pc+5
        karma=1
    if ans == "P" and tah_pc=="P":
        karma=0
    if ans == "N" and tah_pc=="P":
        score_pc=score_pc+10
        karma=1
    print(ans, tah_pc)
    print("Karma",karma)
    print("Tvoje skóre",score, "Skóre PC", score_pc)
    
    pocitadlo=pocitadlo+1
    

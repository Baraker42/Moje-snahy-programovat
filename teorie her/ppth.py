import random
from random import randrange
def copycat (karma,karmaplus):
    karma=karma
    if karma==0:
        tah_pc="N"
    if karma==1:
        tah_pc="P"
    return(tah_pc)

def hustler(karma,karmaplus):
    karma=karma
    tah_pc="P"
    return(tah_pc)

def jesus(karma,karmaplus):
    karma=karma
    tah_pc="N"
    return(tah_pc)

def idk (karma,karmaplus):
    volba=["N","P"]
    tah_pc=random.choice(volba)
    return(tah_pc)

def johnwick(karma,karmaplus):
    if karmaplus==0:
        tah_pc="N"
    if karmaplus>=1:
        tah_pc="P"
    return(tah_pc)
    
    








   
    

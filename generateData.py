import random
import matplotlib.pyplot as plt
from progDyn import *
from outilsLignesBrises import *
def generateData(n,file):
    file = open(file,"w")
    for i in range(n):
        a = i+1
        b = random.randint(1,26)
        file.write(str(a)+" "+str(b)+"\n")
    file.close()
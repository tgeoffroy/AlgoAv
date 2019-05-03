import random

def generateData(n,file):
    file = open(file,"w")
    for i in range(n):
        a = i+1
        b = random.randint(1,101)
        file.write(str(a)+" "+str(b)+"\n")
    file.close() 
 
generateData(15,"DataSet1")

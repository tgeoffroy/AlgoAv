import matplotlib.pyplot as plt
import time
from algoAv import *
from math import *

def progDyn(pointsY, C):
    nbPoints = len(points)
    matrice = []
    
    #Initialisation de zeros
    for i in range(nbPoints):
        matrice.append([])
        for j in range(nbPoints):
            matrice[i].append(0)
    
    #Initialisation des couts avec 0 points intermédiaires (1 brisure)
    for i in range(nbPoints-1):
        matrice[i][i+1] = C
        
        
    for i in range(2, nbPoints):
        for j in range(nbPoints - i):
            min_seg = matrice[j][j+1] + matrice[j+1][j+i]
            if(i>2):
                for l in range(1,i-2):
                    min_seg = min(min_seg, matrice[j][j+1+l]+matrice[j+1+l][j+i])
            
            matrice[j][j+i] = min(min_seg, SDBrisure(Ligne(Point(j+1,pointsY[j]),Point(j+i+1,pointsY[j+i]))) + C)

    return matrice
    

if __name__ == "__main__":
    
    readfile("tst1.txt")
    pointsY = [p.y for p in points]
    
    matrice = progDyn(pointsY, 1.5)
    print(matrice)
	
	
	

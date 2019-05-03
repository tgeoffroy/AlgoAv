import time
from outilsLignesBrises import *
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
            segMin = matrice[j][j+1] + matrice[j+1][j+i]
            
            for l in range(1,i-2):
                segMin = min(segMin, matrice[j][j+1+l]+matrice[j+1+l][j+i])
            
            matrice[j][j+i] = min(segMin, SDBrisure(Ligne(Point(j+1,pointsY[j]),Point(j+i+1,pointsY[j+i]))) + C)

    return matrice
    

if __name__ == "__main__":
    
    readfile("DataSet2")
    pointsY = [p.y for p in points]
    
    t0 = time.time()
    matrice = progDyn(pointsY, 1.5)
    tf = time.time()
    
    print(matrice)
    print(matrice[0][len(points)-1])
    print("Temps de calcul : "+str(tf-t0))
    
	
	
	

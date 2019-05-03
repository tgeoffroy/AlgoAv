import itertools
import matplotlib.pyplot as plt
import time
from algoAv import *

def appligbri(i, Cout):
	Si = calculerSi(i)
	for xi in Si:
		if(satisfaisant(xi)):
			enregistrer(i, xi)
			if soltrouvee():
				if meilleure():
					majValOpt()
			else:
				if encorePossible(i):
					appligbri(i+1, coutCourant)
			defaire(xi)

#Valeur possibles 0 ou 1
def calculerSi(i):
    return [0,1]

def satisfaisant(xi):
    return True

def enregistrer(i, xi):
    global solCourante, coutCourant
    print(solCourante)
    solCourante[i+1] = 1
    coutCourant = cout(generateSolLignes(solCourante), C)
# on a atteint le dernier point
def soltrouvee():
    return solCourante[nbPointsInter] == 1
    
def meilleure():
    return coutCourant < coutMin

def majValOpt():
    global meilleurSol, coutMin
    meilleurSol = solCourante
    coutMin = coutCourant

def encorePossible(i):
	return i < nbPointsInter

def defaire(xi):
    global solCourante, coutCourant
    solCourante = None
    coutCourant = None

def intToBinTable(i):
    s = []
    while i:
        if i & 1 == 1:
            s.append(1)
        else:
            s.append(0)
        i //= 2
    s.reverse()
    return s

if __name__ == "__main__"  :

    readfile("tst1.txt")
    nbPointsInter = len(points) - 2
    tousEssais = [([1]+list(i)+[1]) for i in itertools.product([0, 1], repeat= nbPointsInter)]
    print(tousEssais)
    print(intToBinTable(len(points)))
    
    solCourante = [1] + [0] * (nbPointsInter) + [1]
    meilleurSol = [1] + [0] * (nbPointsInter) + [1]
    
    pointsY = [p.y for p in points]
    coutCourant = 9999999999
    coutMin = 9999999999
    C = 1.5

    t0 = time.time()
    appligbri(0, 0)
    tf = time.time()

    print("\n")
    print("Temps de calcul : "+str(tf-t0))
    print(coutMin,meilleurSol)
    
    
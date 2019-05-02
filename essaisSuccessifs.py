import itertools
import matplotlib.pyplot as plt
import time
from algoAv import *

def appligbri(i):
	Si = calculerSi(i)
	for xi in Si:
		if(satisfaisant(xi)):
			enregistrer(xi)
			if soltrouvee():
				if meilleure():
					majValOpt()
			else:
				if encorePossible():
					appligbri(i+1)
			defaire(xi)


def calculerSi(i):
    ListeDeLignes = []
    for k in range(i):
        ListeDeLignes.append(generateSolLignes(tousEssais[k], pointsY))
    return ListeDeLignes

def satisfaisant(x):
    return True

def enregistrer(x):
    global solCourante, coutCourant
    solCourante = x
    coutCourant = cout(x, C)
    
def soltrouvee():
    return True
    
def meilleure():
    return coutCourant < coutMin

def majValOpt():
    global meilleurSol, coutMin
    meilleurSol = solCourante
    coutMin = coutCourant

def encorePossible():
	return True

def defaire(xi):
    global solCourante, coutCourant
    solCourante = None
    coutCourant = None


if __name__ == "__main__"  :

    readfile("tst1.txt")
    nbPointsInter = len(points) - 2
    tousEssais = [([1]+list(i)+[1]) for i in itertools.product([0, 1], repeat= nbPointsInter)]
    
    pointsY = [p.y for p in points]
    coutCourant = 9999999999
    coutMin = 9999999999
    solCourante = None
    meilleurSol = None
    C = 1.5
    
    t0 = time.time()
    appligbri(len(tousEssais))
    tf = time.time()
    
    print("\n")
    print("Temps de calcul : "+str(tf-t0))
    print(coutMin,meilleurSol)
    print(SDTot(meilleurSol))
    trace2(meilleurSol)
   
import time
from algoAv import *

def appligbri(i):
    Si = calculerSi(i)
    global nbAppel
    nbAppel += 1
    for xi in Si:
        if(satisfaisant(xi)):
            enregistrer(xi)
            if soltrouvee(i):
                if meilleure():
                    majValOpt()
            else:
                if encorePossible(i):
                    appligbri(i+1)
            defaire(xi)



#Valeur possibles 0 ou 1
def calculerSi(i):
	return [0,1]


#a-t-on déjà eu cette configuration (si oui) => False ? 
def satisfaisant(x):
	"""
		Soit toujours True (on ne parcours bien qu'une fois toutes les sols)

			SolTemp = X
	     return dico_sols[SolTemp+[x]] != None

		Soit on vérifie que c'est bien dans un dico de sol
	"""
	return len(X) < longueurSolution

def enregistrer(x):
	X.append(x)

# est ce que X, le vecteur solution est de la forme [1.....1]
def soltrouvee(i):
    return (X[0]==1 and len(X)==longueurSolution and X[-1]==1)
    
# est ce que la sol courante a un cout meilleure, que le cout minimal enregistré ?
def meilleure():
    global coutCourant
    lignes = generateSolLignes(X) # X est la config
    coutCourant = cout(lignes, C)
	# il faut aussi passer les points concernés ATTENTION pas la liste de tous les points : 
	# de pointY[0] à pointY[len[X]]
    
    return coutCourant<coutMin

# est ce que le cout de la solution partielle est toujours < au cout minimal enregistré ?
def encorePossible(i):
    global coutCourant
    lignes = generateSolLignes(X) # X est la config
    coutCourant = cout(lignes, C)
    return (i < longueurSolution) and (coutCourant<coutMin)

# on met à jour la valeur optimale
def majValOpt():
    global Xopt, coutMin
    Xopt = X.copy()
    print("Xopt"+str(Xopt))
    coutMin = coutCourant

# on défait le dernier choix
def defaire(x):
    global X
    X.pop(-1)

if __name__ == "__main__" :
    readfile("DataSet1")
	#dico_sols ou l'on enregistre toutes les sols partielle
    longueurSolution = len(points) # mettre ici le nombre de point du fichier_in
    print(points)
    coutCourant = 999999
    coutMin = 999999999
    C = 1.5
    X = [] # contient la solution en cours de formation
    Xopt = [] # contient la solution optimale
    nbAppel = 0
    
    
    t0 = time.time()
    appligbri(0)
    tf = time.time()

    print("\n")
    print("Temps de calcul : "+str(tf-t0))
    
    print(Xopt,coutMin)
    print(nbAppel)
    trace(Xopt)
    
    
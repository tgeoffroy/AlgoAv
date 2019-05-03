import time
from outilsLignesBrises import *

#Procédure d'essais successifs à trous
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
    lignes = generateSolLignes(X)
    coutCourant = cout(lignes, C)
    return (i < longueurSolution - 1) 
    #(coutCourant<coutMin) and X[0]==1 sont 2 conditions d'élagage

# on met à jour la valeur optimale
def majValOpt():
    global Xopt, coutMin
    Xopt = X.copy()
    coutMin = coutCourant

# on défait le dernier choix
def defaire(x):
    global X
    X.pop(-1)


if __name__ == "__main__" :
    
    #Lecture d'un jeu de données
    readfile("DataSet/DataSet15")
    
	#Initialisation des constantes et variables
    longueurSolution = len(points) #nombre de point du fichier_in
    coutCourant = 999999999  #Infini
    coutMin = 999999999      #Infini
    X = [] #Contient la solution en cours de formation
    Xopt = [] #Contient la solution optimale
    C = 1.5 #Coefficient
    nbAppel = 0 #Nombre d'appels récursifs
    
    #Calcul du temps d'éxécution
    t0 = time.time()
    appligbri(0)
    tf = time.time()

    print("Solution optimale : \n"+str(Xopt))
    print(str(generateSolLignes(Xopt))+"\n")
    print("Cout : "+str(coutMin))
    print("Temps de calcul : "+str(tf-t0))
    print("Nombre d'appels : "+str(nbAppel))
    trace(Xopt)
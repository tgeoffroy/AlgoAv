import itertools

import matplotlib.pyplot as plt

def appligbri(i):
	Si = calculerSi(i)
	for xi in Si:
		if(satisfaisant(xi)):
			enregistrer(xi)
			if soltrouvee():
				if meilleure():
					Y = xi
					majValOpt()
			else:
				if encorePossible():
					appligbri(i+1)
			defaire(xi)




def calculerSi(i):
	return tousEssais[i]

def satisfaisant(x):

def encorePossible():
	return True







def generateAbsOrdIn(data_in):

	"""
		génère les abscisses et ordonées pour les données d'entrée

	"""


	X = []
	Y = data_in
	i=1

	for _ in Y:
		
		X.append(i)
		i+=1

	print("Xin = "+str(X))
	return X, Y

def generateAbsOrdSol(config,data_in):
	"""
		génère les abscisses et ordonées pour une config donnée 
		(ie par quels points on passe)

	"""
	X = []
	Y = []
	nb1 = 0
	for k in config:
		if(k==1):
			nb1+=1

	for i in range(nb1+1):
		
		if(config[i]==1):
			X.append(i+1)
			Y.append(data_in[i])
	
	print("X : "+str(X))
	print("Y : "+str(Y))
	return X, Y


def trace(data_in, config):
	"""
		trace les données d'entrées et une config passant par ces points
	"""
	Xin,Yin = generateAbsOrdIn(data_in)
	Xconf, Yconf = generateAbsOrdSol(config, data_in)
	plt.plot(Xin,Yin,'x')
	plt.plot(Xconf,Yconf, 'red')
	plt.show()


if __name__ == "__main__"  :

	nbPointsInter = 4
	tousEssais = [([1]+list(i)+[1]) for i in itertools.product([0, 1], repeat= nbPointsInter)]

	cout

	print("laaaaa")
	print(calculerSi(3))

import itertools

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

if __name__ == "__main__"  :

	nbPointsInter = 4
	tousEssais = [([1]+list(i)+[1]) for i in itertools.product([0, 1], repeat= nbPointsInter)]

	print("laaaaa")
	print(calculerSi(3))

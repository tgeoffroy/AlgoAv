import itertools


if __name__ == "__main__"  :


	#permet d'avoir toutes les possibilités avec 3 points entre le départ et l'arrivée
	lst = [([1]+list(i)+[1]) for i in itertools.product([0, 1], repeat=3)]
	print(lst)
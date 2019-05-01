import itertools


if __name__ == "__main__"  :

	lst = [([1]+list(i)+[1]) for i in itertools.product([0, 1], repeat=3)]
	print(lst)
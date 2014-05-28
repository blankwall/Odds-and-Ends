import itertools

#generator of strings
def gen_str():
	lst = []
	for i in range (65, 123):
		lst.append(chr(i))

	for i in range(10):
		for K in itertools.product(lst, repeat=i):
			yield "".join(K)
	# return ['a', 'b']



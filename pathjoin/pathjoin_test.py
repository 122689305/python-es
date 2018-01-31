from pathjoin import * 
def test():
	test_aps_list = \
	[
		[
			(('Adim', '18'), ('male')),
			(('Hank', '20'), ('male')),
			(('Andrew', '30'), ('male')),
			(('Alice', '21'), ('female'))
		],
		[
			(('male'), ('Duke', 'General')),
			(('male'), ('James', 'Soldeir')),
			(('female'), ('Ava', 'Scientist'))
		],
		[
			(('Duke', 'General'), (10)),
			(('Duke', 'General'), (11)),
			(('Ava', 'Scientist'), (120)),
			(('Ava', 'Scientist'), (10))
		],
		[
			((10), (1)),
			((10), (2)),
			((120), (1))
		]
	]
	sol = ComputePathJoin(test_aps_list)
	print 'local sensitivity:', sol.solution()
	print 'prelist:', sol.prelist
	print 'postlist', sol.postlist
	print 'preMax:', [max(x.values()) for x in sol.prelist]
	print 'postMax:', [max(x.values()) for x in sol.postlist]
	
	'''
	Test Result:

	local sensitivity: 9
	prelist: [{'male': 3, 'female': 1}, {('Duke', 'General'): 3, ('James', 'Soldeir'): 3, ('Ava', 'Scientist'): 1}, {120: 1, 10: 4, 11: 3}, {1: 5, 2: 4}]
	postlist [{('Adim', '18'): 2, ('Hank', '20'): 2, ('Alice', '21'): 3, ('Andrew', '30'): 2}, {'male': 2, 'female': 3}, {('Duke', 'General'): 2, ('Ava', 'Scientist'): 3}, {120: 1, 10: 2}]
	preMax: [3, 3, 4, 5]
	postMax: [3, 3, 3, 2]
	'''
if __name__ == '__main__':
	test()

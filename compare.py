import es.es_util as es
import pathjoin.pathjoin as pj
import helper
data = \
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
pjs = pj.ComputePathJoin(data).solution()

print pjs

dummy_data = \
	[
		[
			(('Adim', '18'), ('male')),
			(('Hank', '20'), ('male')),
			(('Andrew', '30'), ('male')),
			(('Alice', '21'), ('female')),
			(('Alice1', '21'), ('male')),
			(('Alice5', '21'), ('female')),
			(('Alice6', '21'), ('female'))
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
			((120), (1)),
			((130), (2)),
			((130), (2)),
			((130), (2)),
			((130), (2)),
			((130), (2)),
			((130), (2)),
			((130), (2)),
			((130), (2)),
			((130), (2))
		]
	]

n = 10
k = 5
extreme_data = [[(True, False)] * n]*k

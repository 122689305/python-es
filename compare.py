import es.es_util as es
import pathjoin.pathjoin as pj
import helper
data = \
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
pjs = pj.ComputePathJoin(data)
pj.ComputePathJoin.debug(pjs)
pjs = pjs.solution()
yaml_str = helper.transform(data)
query = helper.gen_query(data)
fn = './tmp_schema.yaml'
with open(fn, 'w') as f:
  f.write(yaml_str)
es = es.k_ES(query, 1, fn)
import os
os.remove(fn)
print yaml_str
print query
print "\n"+"\nResult\n"+"="*20+"\n\n"
print "PathJoin sensitivity: {pjs} \nElastic sensitivity: {es}".format(pjs=pjs, es=es)

import pathjoin.pathjoin as pj
import helper

import sample_data
data = sample_data.dummy_data
data = sample_data.extreme_data

print data

pjs = pj.ComputePathJoin(data)
pj.ComputePathJoin.debug(pjs)
pjs = pjs.solution()
yaml_str = helper.transform(data)
query = helper.gen_query(data)
fn = './schema.yaml'
with open(fn, 'w') as f:
  f.write(yaml_str)
import es.es_util as es
es_res = es.k_ES(query, 1, fn, True, 'test')
#import os
#os.remove(fn)
print yaml_str
print query
print "\n"+"\nResult\n"+"="*20+"\n\n"
print "PathJoin sensitivity: {pjs} \nElastic sensitivity: {es_res}".format(pjs=pjs, es_res=es_res)

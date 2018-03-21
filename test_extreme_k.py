import es.es_util as es
import pathjoin.pathjoin as pj
import helper
import os
import sys

output = open('test_extreme_k.csv', 'a')
n = int(sys.argv[1])
k = int(sys.argv[2])
print n, k
output.write('n,k,es_res\n')
data = [[(True, False)]*n]*k
yaml_str = helper.transform(data)
query = helper.gen_query(data)
fn = './tmp_schema.yaml'
with open(fn, 'w') as f:
  f.write(yaml_str)
es_res = es.k_ES(query, 1, fn)
print es_res
print
output.write("%d,%d,%f\n"%(n,k,es_res))
os.remove(fn)

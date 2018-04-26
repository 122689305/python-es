import json
import sys
import shutil
sys.path.insert(0, '../')

if len(sys.argv) < 4:
    print('[usage] python %s <view_file> <schema_file> <k>'%sys.argv[0])
    exit(1)

view_file, schema_file, k = sys.argv[1:4]
k = int(k)
shutil.copy(schema_file, 'schema.yaml')
import es.es_util as es

views = json.load(open(view_file, 'r'))
for view in views[1:]:
    query, freq = view
    query = str(query)
    query = query.rstrip(';')
    print '='*40
    print 'PROCESSING QUERY: '
    print '='*15 + 'INPUT' + '='*15
    print '[Original Query] %s'%query
    if 'index' in query:
        print 'unknown column: index. Removed'
        query = query.replace('index, ', '')
    if 'h_id' in query and 'JOIN' in query:
        print 'ambiguous column: h_id. Replace'
        query = query.replace(' h_id,', ' housing.h_id,')
    if 'COUNT' not in query:
        print 'Only count can be analized. Add'
        query = query.replace('SELECT ', 'SELECT COUNT(', 1)
        query = query.replace(' FROM', ') FROM', 1)
    print '[Processed Query] %s'%query
    try:
        es_res = es.k_ES(query, k, schema_file, False, 'test')
    except:
        es_res = -1
    view.append(es_res)
    print '='*14 + 'OUTPUT' + '='*15
    print 'k=%d  es=%d'%(k,es_res)
    print

json.dump(views, open('new_'+view_file, 'w'), indent=4)


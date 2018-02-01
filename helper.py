import pandas as pd
from collections import Counter

# return yaml
def transform(data):
  yaml_head_f = """---
databases:
- database: "{database}"
  dialect: "{dialect}"
  namespace: "{namespace}"
  tables:
"""
  yaml_table_f = """  - table: "{table}"
    columns:
"""
  yaml_column_f = """    - name: "{name}"
      maxFreq: {maxFreq}
"""
  column_names = ["R"+str(x) for x in range(len(data))]
  data = [[reduce(lambda r, n: r+n, map(lambda a: list(a) if type(a) == tuple else [a], y), []) for y in x] for x in data]
  yaml_data = [pd.DataFrame.from_records(x) for x in data]
  yaml_data = [x.apply(lambda y: max(Counter(y).values()), axis=0) for x in yaml_data]
  yaml_head = yaml_head_f.format(database="test", dialect="vertica", namespace="public")
  yaml_str = yaml_head + "".join(yaml_table_f.format(table="R"+str(i)) +  "".join(yaml_column_f.format(name="col"+str(j), maxFreq=str(yaml_data[i][j])) for j in range(len(yaml_data[i]))) for i in range(len(yaml_data)))  
  return yaml_str

def gen_query(data):
  def cols2label(cols, lr):
    #lr = 0 => l
    #lr = 1 => r
    cols = [list(x) if type(x) == tuple else [x] for x in cols]
    if lr == 0:
      return ["col"+str(i) for i in range(len(cols[0]))]
    else:
      return ["col"+str(len(cols[0]) + i) for i in range(len(cols[1]))]

  join_head = "R0"
  join_clause_f = " JOIN {tr} ON {join_cond}"
  join_cond_f = "{tl}.{cl} = {tr}.{cr}"
  join_and_f = " AND "

  query = "SELECT COUNT(*) FROM "
  query += join_head
  for i in range(len(data)-1):
    tl = data[i]
    tr = data[i+1]
    tl_cls = cols2label(tl[0], 1)
    tr_cls = cols2label(tr[0], 0)
    join_cond = join_and_f.join(join_cond_f.format(tl="R"+str(i), tr="R"+str(i+1), cl=tl_cls[j], cr=tr_cls[j]) for j in range(len(tl_cls)))
    join_clause = join_clause_f.format(tr="R"+str(i+1), join_cond=join_cond)
    query += join_clause
  return query

if __name__ == '__main__':
  transform([[((1,2),(3)), ((4,5),(6))], [((2,4),(5))]]); 

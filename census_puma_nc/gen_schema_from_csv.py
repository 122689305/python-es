#nc_houses.csv  nc_persons2.csv
import sys
import pandas as pd

def gen_tables():
    csv_files = sys.argv[1::2]
    table_names = sys.argv[2::2]
    tables = []
    for csv_file, table_name in zip(csv_files, table_names):
        print "processing file:%s with table %s"%(csv_file, table_name)
        tables.append({'table':table_name, 'cols':{}})
        df = pd.read_csv(csv_file)
        for col in df.columns.values:
            freq=max(df[col].value_counts())
            tables[-1]['cols'][col] = freq
    return tables

def gen_schema(tables):
    schema_head = '''---
databases:
- database: "test"
  dialect: "vertica"
  namespace: "public"
  tables:
'''
    schema_table = '  - table: "%s"\n    columns:\n'
    schema_col = '    - name: "%s"\n      maxFreq: %d\n'

    schema = schema_head
    for table in tables:
        print table
        schema += schema_table%table['table']
        for col, freq in table['cols'].items():
            schema += schema_col%(col, freq)
    return schema

def write_schema(fn, schema):
    with open(fn, 'w') as f:
        f.write(schema)

if __name__ == '__main__':
    tables = gen_tables()
    schema = gen_schema(tables)
    write_schema('gen_schema.yaml', schema)

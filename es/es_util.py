import jnius_config
import os
path = os.path.abspath(os.path.dirname(__file__))
version = '0.1.3'
if version == '0.1.2':
  jar_path = os.path.join(path, 'sql-differential-privacy-0.1.2-SNAPSHOT-jar-with-dependencies.jar')
elif version == '0.1.3':
  jar_path = os.path.join(path, 'sql-differential-privacy-0.1.3-SNAPSHOT-jar-with-dependencies.jar')
print path
print jar_path
jnius_config.set_classpath(jar_path)
import jnius

System = jnius.autoclass('java.lang.System')

ESAnalyzer = jnius.autoclass('com.uber.engsec.dp.analysis.differential_privacy.ElasticSensitivityAnalysis')
QueryParser = jnius.autoclass('com.uber.engsec.dp.sql.QueryParser$')
parseToRelTree = getattr(QueryParser, "MODULE$").parseToRelTree

'''
if version == '0.1.2':
  DPUtils = jnius.autoclass('com.uber.engsec.dp.util.DPUtils$')
elif version == '0.1.3':
  DPUtils =
elasticSensitivity = getattr(DPUtils, "MODULE$").elasticSensitivity
'''

if version == '0.1.3':
  Schema = jnius.autoclass('com.uber.engsec.dp.schema.Schema$')
#print Schema.__dict__
  getDatabase = getattr(Schema, "MODULE$").getDatabase

def k_ES(query, k, yaml_path, query_debug = False, db = None):
  System.setProperty("schema.config.path", yaml_path)
  System.setProperty("query.debug", "true" if query_debug else "false")

  if db is not None:
    database = getDatabase(db)

  analysis = ESAnalyzer()
  parser = parseToRelTree

  if db is not None:
    tree = parser(query, database)
  else:
    tree = parser(query)

  analysis.setK(k)
  if db is not None:
    result = analysis.analyzeQuery(tree, database).colFacts()
  else:
    result = analysis.analyzeQuery(tree).colFacts()
  result = result.head().sensitivity().get()
  return result

'''
def original_k_ES(query, k, yaml_path):
  System.setProperty("schema.config.path", yaml_path)

  result = elasticSensitivity(query, k)
  return result
'''




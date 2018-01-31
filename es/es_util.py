import jnius_config
import os
path = os.path.abspath(os.path.dirname(__file__))
jar_path = os.path.join(path, 'sql-differential-privacy-0.1.2-SNAPSHOT-jar-with-dependencies.jar')
jnius_config.set_classpath(jar_path)
import jnius

System = jnius.autoclass('java.lang.System')

ESAnalyzer = jnius.autoclass('com.uber.engsec.dp.analysis.differential_privacy.ElasticSensitivityAnalysis')
QueryParser = jnius.autoclass('com.uber.engsec.dp.sql.QueryParser$')
parseToRelTree = getattr(QueryParser, "MODULE$").parseToRelTree

DPUtils = jnius.autoclass('com.uber.engsec.dp.util.DPUtils$')
elasticSensitivity = getattr(DPUtils, "MODULE$").elasticSensitivity


def k_ES(query, k, yaml_path):
  System.setProperty("schema.config.path", yaml_path) 

  analysis = ESAnalyzer()
  parser = parseToRelTree

  tree = parser(query)
  analysis.setK(k)
  result = analysis.analyzeQuery(tree).colFacts()
  result = result.head().sensitivity().get()
  return result

def original_k_ES(query, k, yaml_path):
  System.setProperty("schema.config.path", yaml_path) 

  result = elasticSensitivity(query, k)
  return result




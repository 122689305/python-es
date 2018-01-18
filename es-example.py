import jnius_config
jar_path = 'sql-differential-privacy-0.1.2-SNAPSHOT-jar-with-dependencies.jar'
jnius_config.set_classpath(jar_path)
import jnius

DPExample = jnius.autoclass("com.uber.engsec.dp.util.DPExample$")
print(DPExample)
getattr(DPExample, "MODULE$").main(list(""))

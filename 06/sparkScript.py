from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("appName").getOrCreate()
sc = spark.sparkContext

txt = sc.textFile('/home/playtika/scenarios/06/textFile.txt')
print('Lines Count for File textFile.tst: ' + str(txt.count()))

sc.stop()

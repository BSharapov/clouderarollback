from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.conf import SparkConf

conf = SparkConf()
conf.setMaster("local").setAppName("My app")

sc = SparkContext('local')
spark = SparkSession(sc)

dataList = [("Java", 20000), ("Python", 100000), ("Scala", 3000)]
rdd=spark.sparkContext.parallelize(dataList)
print(rdd.collect())

print( "The issue was solved, well done!")

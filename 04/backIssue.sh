#!/bin/bash

sudo rm -rf sparkScript.py
echo "st = [12, 23, 34, 45, 56, 67, 78, 89, 90]
rdd1 = sc.parallelize(list)
rdd2 = rdd1.map(lambda x: x/2)
print(rdd2.collect())
print('The issue was solved, well done!')" >> sparkScript.py

export PYSPARK_PYTHON=/usr/bin/python2.7
export HADOOP_CONF_DIR=/opt/cloudera/parcels/CDH-6.3.2-1.cdh6.3.2.p0.1605554/lib/spark/conf/yarn-conf
export HADOOP_USER_NAME=hdfs
export SPARK_HOME=/opt/cloudera/parcels/CDH-6.3.2-1.cdh6.3.2.p0.1605554/lib/spark

$SPARK_HOME/bin/spark-submit \
--master yarn-client \
sparkScript.py

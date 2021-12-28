#!/bin/bash

export PYSPARK_PYTHON=/usr/bin/python2.7
export HADOOP_CONF_DIR=/opt/cloudera/parcels/CDH-6.3.2-1.cdh6.3.2.p0.1605554/lib/spark/conf/yarn-conf
export HADOOP_USER_NAME=hdfs
export SPARK_HOME=/opt/cloudera/parcels/CDH-6.3.2-1.cdh6.3.2.p0.1605554/lib/spark

$SPARK_HOME/bin/spark-submit \
--master yarn-client \
sparkScript.py

#!/bin/bash

export PYSPARK_PYTHON=/usr/bin/python2.7
export HADOOP_CONF_DIR=/opt/cloudera/parcels/CDH-6.3.2-1.cdh6.3.2.p0.1605554/lib/spark/conf/yarn-conf
export HADOOP_USER_NAME=ply1_user
export SPARK_HOME=/opt/cloudera/parcels/CDH-6.3.2-1.cdh6.3.2.p0.1605554/lib/spark

sudo userdel -r ply1_user
id -u ply1_user &>/dev/null

if [ $? -eq 1 ]; then
	sudo -u hdfs hdfs dfs -chmod o-x /user
fi

$SPARK_HOME/bin/spark-submit \
--master yarn-client \
sparkScript.py

sudo -u hdfs hdfs dfs -chmod o+x /user

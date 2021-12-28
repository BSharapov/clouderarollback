#!/bin/bash

sudo rm -rf sparkScript.py
echo "
export PYSPARK_PYTHON=/usr/bin/python2.7
export SPARK_HOME=/opt/cloudera/parcels/CDH-6.3.2-1.cdh6.3.2.p0.1605554/lib/spark

$SPARK_HOME/bin/spark-submit \
--master yarn-client \
--driver-memory 4g \
--executor-memory 16g \
sparkScript.py

#!/bin/bash
export HIVE_HOME=/opt/cloudera/parcels/CDH-6.3.2-1.cdh6.3.2.p0.1605554/bin/

$HIVE_HOME/beeline -u jdbc:hive2://localhost:10000/default -n hdfs -p naya -e 'select * from events.events_log'

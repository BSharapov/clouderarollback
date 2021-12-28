---------------------------------
-- Playtika Cloudera Simulator --
---------------------------------

-- Scenerio 06 --

- SSH to the Cloudera Simulator using the playtika user.
- Navigate to the following path: /home/playtika/scenarios/06
- Run the following script: createIssue.sh
- Script Command:
   export PYSPARK_PYTHON=/usr/bin/python2.7
   export SPARK_HOME=/opt/cloudera/parcels/CDH-6.3.2-1.cdh6.3.2.p0.1605554/lib/spark

   $SPARK_HOME/bin/spark-submit \
   --master yarn-client \
   --queue my_pool \
   sparkScript.py

- Specify the cause of the error in the project notebook for scenario 06.
- Scenario Objective(s): Run the command above with no errors (not the script).
- Additional objectives:
  - Extract the Spark job name (e.g. application_1637959403721_0071)
  - Locate the job at the YARN ResourceManager web UI, add a screenshot for this specific job in the project notebook.
  - Locate the relevant log file holding the job information.
- Script success message: "Lines Count for File textFile.tst: 104"
- Scenario Solution - The solution should be mentioned in the solutions notebook..

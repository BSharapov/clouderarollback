---------------------------------
-- Playtika Cloudera Simulator --
---------------------------------

-- Scenerio 08 --

- SSH to the Cloudera Simulator using the playtika user.
- Navigate to the following path: /home/playtika/scenarios/08
- Run the following script: createIssue.sh
- Script Command:
  $ export PYSPARK_PYTHON=/usr/bin/python2.7
  $ export SPARK_HOME=/opt/cloudera/parcels/CDH-6.3.2-1.cdh6.3.2.p0.1605554/lib/spark

  $SPARK_HOME/bin/spark-submit \
   --master yarn-client \
   --driver-memory 4g \
   --executor-memory 16g \
   sparkScript.py

- Specify the cause of the error.
- Scenario Objective(s): The script should complete with no errors.
- Script success message: "The issue was solved, well done!"
- Scenario Solution - The solution should be mentioned in the solutions notebook (note that the scenario may hold nested issues - more than one issue).

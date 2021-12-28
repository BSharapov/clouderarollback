---------------------------------
-- Playtika Cloudera Simulator --
---------------------------------

-- Scenerio 20 --

- SSH to the Cloudera Simulator using the playtika user.
- Navigate to the following path: /home/playtika/scenarios/20
- To simulate a human mistake of accidentally deleting a Hive table, run the following command:
  beeline -u jdbc:hive2://localhost:10000/default -n hdfs -p naya -e 'drop table classicmodels.employees'

- Specify what happened from HDFS and the metastore perspectives in the project notebook for scenario 20.
- Scenario Objective(s): Restore the deleted table to its previous state - the table data should be available using SQL.
- Scenario Solution - The solution including all used syntax should be mentioned in the solutions notebook.

---------------------------------
-- Playtika Cloudera Simulator --
---------------------------------

-- Scenerio 14 --

- SSH to the Cloudera Simulator using the playtika user.
- Navigate to the following path: /home/playtika/scenarios/14
- Run the following command:
  - beeline -u jdbc:hive2://localhost:10000/default -n hdfs -p naya -f hiveStatement.sql

- Specify the cause of the error in the project notebook for scenario 14.
- Note that the Hive SQL statement can be run using HUE as well. 
- Scenario Objective(s): The SQL statement should complete successfully.
- Scenario Solution - The solution should be mentioned in the solutions notebook.

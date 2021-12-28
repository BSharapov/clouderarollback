---------------------------------
-- Playtika Cloudera Simulator --
---------------------------------

-- Scenerio 02 --

- SSH to the Cloudera Simulator using the playtika user.
- Navigate to the following path: /home/playtika/scenarios/02
- Run the following script: createIssue.sh
- Open HUE and select Hive as the SQL engine
- Run the following query:
  
   select * from classicmodels.orders where ordernumber = 10103;

- Specify the encountered issue in the project notebook for scenario 02.
- Scenario Objective(s): The SQL statement should be completed successfully.
- Scenario Solution - The solution should be mentioned in the solutions notebook.

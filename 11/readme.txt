---------------------------------
-- Playtika Cloudera Simulator --
---------------------------------

-- Scenerio 11 --

- SSH to the Cloudera Simulator using the playtika user.
- Navigate to the following path: /home/playtika/scenarios/11
- Run the following script: createIssue.sh
- Open HUE and select Hive as the SQL engine.
- Run the following query:
   select customernumber, 
          count(*) as custCount
   from classicmodels.orders
   group by customernumbe
   order by custCount desc;

- Specify the encountered issue in the project notebook for scenario 11.
- Scenario Objective(s): Make sure that all Cloudera Services are up and running.
- Scenario Solution - The solution should be mentioned in the solutions notebook.

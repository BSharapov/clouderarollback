---------------------------------
-- Playtika Cloudera Simulator --
---------------------------------

-- Scenerio 18 --

- SSH to the Cloudera Simulator using the playtika user.
- Navigate to the following path: /home/playtika/scenarios/18
- Run the following script: createIssue.sh
- Open HUE and select Hive as the SQL engine.
- Run the following query:
   SELECT t.*, 
          DATEDIFF(orderdate, prev_order) AS days_diff
   FROM
       (SELECT ordernumber, 
               orderdate, 
               customernumber,
               LAG(orderdate) OVER(PARTITION BY customernumber 
               ORDER BY orderdate) AS prev_order
       FROM classicmodels.orders) t
   ORDER BY ordernumber;

- Specify the encountered issue in the project notebook for scenario 18.
- Scenario Objective(s): The SQL statement should be completed successfully.
- Scenario Solution - The solution should be mentioned in the solutions notebook.

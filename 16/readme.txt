---------------------------------
-- Playtika Cloudera Simulator --
---------------------------------

-- Scenerio 16 --

- Open HUE (user: 'playtika') and select Hive as the SQL engine.
- Run the following SQL statement:
   select * from default.take_away_orders
   where year(order_date) = 2016
   and month(order_date) between 1 and 3;

- Specify what is the core issue from performance perspectives, when applying the above SQL statement in the project notebook for scenario 16.
- In addition, mention how you can provide an indication to your findings in the project notebook for scenario 16.
- Scenario Assumption: 
  - The majority of the queries against the default.take_away_orders table (79999 records) are being filtered by the following functions:
    - year(order_date)
    - month(order_date)
- Scenario Objective(s): Create a better solution for the use-case described in this scenario based on the AVRO file format.
- Scenario Solution:
  - The solution should be mentioned in the solutions notebook including the all applied code/syntax (note that there be more than one issue for this scenario).
  - Provide a comparison between the current state and to your suggested solution.

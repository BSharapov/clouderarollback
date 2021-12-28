---------------------------------
-- Playtika Cloudera Simulator --
---------------------------------

-- Scenerio 19 --

- Open HUE (user: 'playtika') and select Hive as the SQL engine.
- Create an EXTERNAL TABLE with the following details:
  - Create a new database named (using the if not exists statement): 
    - playtika
  - Table Name: 
    - ingame_purchases (using the playtika database)
  - Specify the following columns:
    - game_id int
    - player_id string
    - purchese_timestamp timestamp
    - purchese_amount int 
  - Store the table using the default file format.
- SSH to the Cloudera Simulator using the playtika user.
- Navigate to the following path: /home/playtika/scenarios/19
- Copy the ingame_purchases.data file into the HDFS table path.
- Run the following verification SQL statement:
  select * from playtika.ingame_purchases;

- Specify the cause of the error in the project notebook for scenario 19.
- Scenario Objective(s): The verification SQL statement should return the ingame_purchases.data file data (1000 records).
- Scenario Solution - The solution should be mentioned in the solutions notebook including all of the required steps until the required output.

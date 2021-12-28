---------------------------------
-- Playtika Cloudera Simulator --
---------------------------------

-- Scenerio 15 --

-- Open HUE (user: 'playtika') and select Hive as the SQL engine.
-- Create an EXTERNAL TABLE with the following details:
   - Create a new database named: 
     - playtika
   - Table Name: 
     - player_scores (using the playtika database)
   - Specify the following columns:
     - game_id int
     - player_id string
     - score_timestamp timestamp
     - player_score int 
   - Store the table using the PARQUET file format.
- SSH to the Cloudera Simulator using the playtika user.
- Navigate to the following path: /home/playtika/scenarios/15
- Copy the player_scores.data file into the HDFS /tmp path.
- Use the LOAD DATA INPATH statement to move the data into the table.
- Run the following verification SQL statement:
  select * from playtika.games_socre;

- Specify the cause of the error in the project notebook for scenario 15.
- Scenario Objective(s): The verification SQL statement should return the player_scores.data file data (1000 records).
- Scenario Solution - The solution should be mentioned in the solutions notebook including all of the required steps until the required output.

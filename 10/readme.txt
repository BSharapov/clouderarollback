---------------------------------
-- Playtika Cloudera Simulator --
---------------------------------

-- Scenerio 10 --

- SSH to the Cloudera Simulator using the playtika user.
- Navigate to the following path: /home/playtika/scenarios/10
- Run the following script: hiveQuery.sh
- The script runs the following command:
  - beeline -u jdbc:hive2://localhost:10000/default -n hdfs -p naya -e 'select * from events.events_log'

- Scenario Objective(s):
  - The event_timestamp column returns a UNIX Time value.
  - Change the UNIX Time value to a date format such as: YYYY-MM-DD HH:MI:SS.
  - Using Hive, create a VIEW which stores the required date format.
- Script success message: The output of the view should return a normal date format.
- Scenario Solution - The solution should be mentioned in the solutions notebook including Hive syntax for the VIEW creation.

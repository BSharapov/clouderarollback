---------------------------------
-- Playtika Cloudera Simulator --
---------------------------------

-- Scenerio 12 --

- SSH to the Cloudera Simulator using the playtika user.
- Navigate to the following path: /home/playtika/scenarios/12
- Run the following script: createIssue.sh
- Note: The createIssue.sh script should run for a few minutes, you should not proceed to the next step until the script completes (new prompt line).
- Open HUE using the playtika user and select Hive as the SQL engine.
- Run the following query:
    select ordernumber,
           orderdate,
           status,
           uuid,
           customernumber
    from classicmodels.ords
    where uuid > '252d261840ed2d15ef1ce5aa2877012bc5c4'
    order by orderdate desc;

- Specify the encountered issue in the project notebook for scenario 12.
- Provide indication for your findings from log files or any other source.
- Scenario Objective(s): The SQL query should be completed successfully.
- Rollback Option: This scenario supports a rollback option in case that the issue was not resolved (or skipping this scenario), rollback script - rollbackIssue.sh
- Scenario Solution - The solution should be mentioned in the solutions notebook.

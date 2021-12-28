---------------------------------
-- Playtika Cloudera Simulator --
---------------------------------

-- Scenerio 07 --

- Scenario 7
- SSH to the Cloudera Simulator using the playtika user.
- Navigate to the following path: /home/playtika/scenarios/07
- Run the following script: createIssue.sh
- Login into HUE with playtika user and select Hive as the SQL engine.
- Run the following query:
   select emp.firstname, 
          emp.lastname, 
          mgr.firstname, 
          mgr.lastname
   from classicmodels.employees emp join classicmodels.employees mgr
   on mgr.employeenumber = emp.reportsto;

- Specify the encountered issue in the project notebook for scenario 07.
- What was the error?
- Mentioned all encountered issues 
- Scenario Objective(s): The SQL statement should be completed successfully.
- Scenario Solution - The solution should be mentioned in the solutions notebook.

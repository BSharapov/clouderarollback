---------------------------------
-- Playtika Cloudera Simulator --
---------------------------------

-- Scenerio 03 --

- SSH to the Cloudera Simulator using the playtika user.
- Navigate to the following path: /home/playtika/scenarios/03
- Launch PySpark by running: pyspark
- From PySpark run the following command:
     file = sc.textFile('/home/playtika/scenarios/03/file1.log')
     fileRead = file.collect()

     for v in fileRead:
     print(v)

- Specify the error(s) in the project notebook for scenario 03.
- Multiple errors/issues may be encountered in this scenario.
- Scenario Objective(s): Print the content of the file1.log file.
- Script success message: "You solved scenario #3, well done!"
- Scenario Solution - The solution should be mentioned in the solutions notebook.

---------------------------------
-- Playtika Cloudera Simulator --
---------------------------------

-- Scenerio 21 --

- SSH to the Cloudera Simulator using the playtika user.
- Navigate to the following path: /home/playtika/scenarios/21
- Run the following script: createIssue.sh
- Create a Kafka topic using the following command:
   kafka-topics --create \
   --zookeeper localhost:2181/kafka \
   --replication-factor 1 \
   --partitions 1 \
   --topic playtika-topic-01

- Specify the cause of the error in the project notebook for scenario 21.
- Scenario Objective(s): Run the Kafka topic creation successfully.
- Scenario Solution - The solution should include all used syntax in the solutions notebook.

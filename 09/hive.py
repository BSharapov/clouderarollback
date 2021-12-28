from pyhive import hive

conn = hive.Connection(host='localhost ', port=10000, username='hdfs')

cursor = conn.cursor() 
cursor.execute("select * from employee limit 10")

for result in cursor.fetchall():
	print(result)

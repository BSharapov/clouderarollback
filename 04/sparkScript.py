st = [12, 23, 34, 45, 56, 67, 78, 89, 90]
rdd1 = sc.parallelize(list)
rdd2 = rdd1.map(lambda x: x/2)
print(rdd2.collect())
print('The issue was solved, well done!')

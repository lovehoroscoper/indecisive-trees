import bsddb
import time

db = bsddb.btopen('testdb.db', 'c')
f = open('user.txt', 'r')
i = 0
for line in f:
	line = line.strip()
	tokens = line.split('\t')
	try:
		db[tokens[0]] = tokens[1]
		i += 1
	except ValueError:
		continue
db.sync()
print "total time: " + str(time.time() - start_time) + " elements: " + str(i)

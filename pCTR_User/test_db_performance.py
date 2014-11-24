import bsddb
import time

db = bsddb.btopen('testdb.db', 'c')
f = open('user.txt', 'r')
i = 0
for line in f:
	line = line.strip()
	tokens = line.split('\t')
	line_id = tokens[0]
	v = db[line_id]
print "total time: " + str(time.time() - start_time) + " elements: " + str(i)

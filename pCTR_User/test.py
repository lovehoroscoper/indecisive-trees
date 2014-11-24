import time

start_time = time.time()
d = {}
f = open('user.txt', 'r')
i = 0
for line in f:
	line = line.strip()
	tokens = line.split('\t')
	try:
		k = int(tokens[0])
		v = float(tokens[1])
		d[k] = v
		i += 1
	except ValueError:
		continue
print "total time: " + str(time.time() - start_time) + " elements: " + str(i)
print "max key is: " + str(max(d.keys()))

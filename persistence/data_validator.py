#!/usr/bin/env python

i = open('agg_out2.txt', 'r')
for line in i:
	line = line.strip()
	fields = line.split('\t')
	if len(fields) != 25:
		print fields
		break
#!/usr/bin/env python

'''
Validation for the output of feature_generator.py. The magic number
for the feature count is 25, but should be changed accordingly if
feature_generator.py is modified.

Input: FEATURE_COUNT - expected number of features
       INPUT - input feature matrix

Output: none

Author: Alan Kao
'''

INPUT = 'agg_output.txt'
FEATURE_COUNT = 25

i = open(INPUT, 'r')
for line in i:
	line = line.strip()
	fields = line.split('\t')
	if len(fields) != FEATURE_COUNT:
		print 'feature count error'
		print fields
		break
	try:
		[float(x) for x in fields]
	except ValueError:
		print 'float cast error'
		print fields
		break

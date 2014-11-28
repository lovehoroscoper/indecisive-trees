#!/usr/bin/env python

'''
Author: Alan Kao

Performs instance sampling on the raw training set. Sessions
with no clicks are ignored. Also splits the instances into
positive and negative instances accordingly.

Input: PERCENTAGE - likelihood of choosing an instance
       training - Training data to be passed in via stdin
Output: samples - sampled data with an additional pos/neg attr
'''

import random
from os import sys

PERCENTAGE = 0.20

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')

    clicks = None
    impressions = None
    try:
    	clicks = int(fields[0])
    	impressions = int(fields[1])
    except ValueError:
    	continue

    if impressions == 0 or clicks == 0:
    	continue

    try:
    	userid = int(fields[11])
    	if userid == 0:
    		continue
    except ValueError:
    	pass

    for i in range(impressions):
    	if random.random() > PERCENTAGE:
    		continue
    	# positive instance == 1
    	if random.random() < (float(clicks) / float(impressions)):
    		print "1\t" + line
    	else:
    		print "0\t" + line
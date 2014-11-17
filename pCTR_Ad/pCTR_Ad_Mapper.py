#!/usr/bin/env python

'''
Mapper to compute the pCTR for ad ID.

Input: training set
Output: map output to compute pCTR

Author: Alan Kao
'''

import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')
    print '%s\t%s\t%s' % (fields[3], fields[0], fields[1]) # ad ID, click, impressions

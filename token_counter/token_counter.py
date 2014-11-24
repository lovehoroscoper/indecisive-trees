#!/usr/bin/env python

'''
Generic function to compute the number of tokens in a list. Primarily
used for the YYY_id.txt data sets.

Input: ID token dataset
Output: ID-num token dataset

Author: Anna Zhang
'''

import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')
    tokens = fields[1].split('|')
    print '%s\t%s' % (fields[0], len(tokens))

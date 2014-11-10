#!/usr/bin/env python


import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')
    print '%s\t%s\t%s' % (fields[11], fields[0], fields[1]) # user ID, click, impressions

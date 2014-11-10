#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')
    tokens = fields[1].split('|')
    print '%s\t%s' % (fields[0], len(tokens))

#!/usr/bin/env python

from operator import itemgetter
import sys

ALPHA = 0.05
BETA = 75

current_user_id = None
user_id = None
clicks = 0
impressions = 0

for line in sys.stdin:
    line = line.strip()
    user_id, click, impr = line.split('\t')

    if current_user_id == user_id:
        clicks += int(click)
        impressions += int(impr)
    else:
        if current_user_id:
            pCTR = float(int(clicks) + ALPHA * BETA) / (float(int(impressions) + BETA))
            print '%s\t%s\t%s' % (current_user_id, pCTR)
        clicks = int(click)
        impressions = int(impr)
        current_user_id = user_id
        

# do not forget to output the last word if needed!
if current_user_id == user_id:
    pCTR = float(int(clicks) + ALPHA * BETA) / (float(int(impressions) + BETA))
    print '%s\t%s\t%s' % (current_user_id, pCTR)

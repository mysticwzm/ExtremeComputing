#!/usr/bin/python

import sys
from operator import itemgetter

index = 0
for line in sys.stdin:
    count,site = line.strip().split('\t')
    #output the top 10 hosts which produced the most 404 HTTP errors
    if index < 10:
        index = index + 1
        print site
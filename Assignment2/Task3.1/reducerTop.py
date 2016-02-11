#!/usr/bin/python

import sys
from operator import itemgetter

#find the page from 10 candidates/files
max_page = ''
max_count = 0
for line in sys.stdin:
    page,value = line.strip().split('\t')
    value = int(value)
    if value > max_count:
        max_count = value
        max_page = page
print max_page
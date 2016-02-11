#!/usr/bin/python

import sys
from operator import itemgetter

prePage,value = sys.stdin.readline().strip().split('\t')
count = int(value)
max_count = 0
max_page = ''
for line in sys.stdin:
    #get the name of page and its visited times
    page,value = line.strip().split('\t')
    value = int(value)
    if page == prePage:
        count = count + value
    #compare the total visited times with the maximum visited times
    #if it is more than the maximum visited times, update it
    else:
        if count > max_count:
            max_count = count
            max_page = prePage
        prePage = page
        count = value
#compare the total visited times of the last page with maximum visited times 
if count > max_count:
    max_count = count
    max_page = prePage
#output the page which has been visited most
print '%s\t%s' % (max_page,max_count)
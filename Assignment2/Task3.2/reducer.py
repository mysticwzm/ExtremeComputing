#!/usr/bin/python

import sys
from operator import itemgetter

#get the name of host and its number of 404 reply
preSite,preValue = sys.stdin.readline().strip().split('\t')
count = int(preValue)
for line in sys.stdin:
    site,value = line.strip().split('\t')
    value = int(value)
    #add up the number of 404 replys of the same host
    if preSite == site:
        count = count + value
    #output the total number of 404 replys of the previous host and its name
    #and start the statistics for the new host
    else:
        print '%s\t%s' % (count,preSite)
        count = value
        preSite = site
#output the total number of 404 replys of the last host and its name 
print '%s\t%s' % (count,preSite)
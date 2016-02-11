#!/usr/bin/python

import sys

for line in sys.stdin:
    count,site = line.strip().split('\t')
    #in order to sort from high to low, I use 9999999 which is a 'big' number
    #to minus the number of 404 replys of each host
    #the bigger the number of 404 replys is, the smaller result got after the minus
    count = str(9999999 - int(count))
    print '%s\t%s' % (count,site)
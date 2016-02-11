#!/usr/bin/python

import sys
from operator import itemgetter

#index is used to count top20 number
index = 0;
#input from STDIN
for line in sys.stdin:
    if index < 20:
        index = index + 1
        key,value = line.strip().split('\t',1);
        #in order to restore the original number, use 999999999 to minus key again
        key = 9999999999 - int(key)
        print '%s\t%s' % (value,key)
    
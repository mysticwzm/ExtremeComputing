#!/usr/bin/python

import sys
from operator import itemgetter

#prev line
prevWord = " "
#row and word counter
totalWord = 0
totalRow = 0
#input from STDIN
for line in sys.stdin:
    #split the key and value(the number of words in line)
    word,value = line.split('\t',1)
    #change value to integer type
    value = int(value)
    #increase row counter by 1 and word counter by value
    totalWord = totalWord + value
    totalRow = totalRow + 1
#output total row and word number
print '%d\t%d' % (totalRow,totalWord)
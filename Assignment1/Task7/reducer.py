#!/usr/bin/python

import sys
from operator import itemgetter

#initial key is 0000
prevKey = "0000"
outputString = ""
for line in sys.stdin:
    key,value = line.strip().split('\t',1)
    key = key[:4]
    if prevKey == key:
    #if it is in tha same row, add the value to outputString
        outputString = outputString + value + " "
    else:
    #else it is the start of next row,output the former row
    #and then clear the outputString to store new row
        print outputString
        prevKey = key
        outputString = "" + value + " "
#output last row
print outputString

#reducer, I just need to get the first 4 numbers in key
#which represents the row number
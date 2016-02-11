#!/usr/bin/python

import sys
from operator import itemgetter

#read the first line of standard input and split
#to ensure the first sequence
prevSequence,totalCount = sys.stdin.readline().strip().split('\t',1)
totalCount = int(totalCount)
sequence = ''
#input from STDIN
for line in sys.stdin:
    #split the line into key(sequence) and value
    sequence,value = line.strip().split('\t',1)
    value = int(value)
    #same sequece, increase the totalCount by value
    if prevSequence == sequence:
        totalCount = totalCount + value
        continue
    else:
        #if it is another sequence, then output the former sequence
        printSequence = "'" + prevSequence.split()[0] + "', '" \
        + prevSequence.split()[1] +"', '" + prevSequence.split()[2] + "'"
        print '%s\t%d' % (printSequence,totalCount)
        prevSequence = sequence
        totalCount = value
#output the last sequence
if prevSequence == sequence:
    printSequence = "'" + prevSequence.split()[0] + "', '" \
    + prevSequence.split()[1] +"', '" + prevSequence.split()[2] + "'"
    print '%s\t%d' % (printSequence,totalCount)
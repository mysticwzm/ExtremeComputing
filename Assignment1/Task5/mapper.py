#!/usr/bin/python

import sys

#dictionary to store sequence as a combiner
d = {}
#input from standard input
for line in sys.stdin:
    #split and make sequence
    tokens = line.strip().split()
    for i in range(0,len(tokens) - 2):
        sequences = tokens[i] + ' ' + tokens[i+1] + ' ' + tokens[i+2]
        #if sequence has in d, increase its value by 1
        if sequences in d:
            d[sequences] = d[sequences] + 1
        #else add the sequence to d
        else:
            d.update({sequences:1})
#output all elements in d to reducer
for key in d:
    print '%s\t%s' % (key,d[key])
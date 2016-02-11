#!/usr/bin/python

import sys

for line in sys.stdin:
    tokens = line.strip().split()
    if len(tokens) == 3:
        #if len(tokens)==3 means it is a string contains name
        print '%s\t%s' % (tokens[1],tokens[2])
    else:
        #else len(tokens)==4 means it is a string contains mark
        print '%s\t%s' % (tokens[2]," (" + tokens[1] + "," + tokens[3] + ") ")
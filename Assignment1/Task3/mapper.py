#!/usr/bin/python

import sys

#input from standard input
for line in sys.stdin:
    #remove the whitespace in line
    line = line.strip()
    #output the line and number of words in this line
    #as key and value
    print '%s\t%s' % (line,len(line.split()))
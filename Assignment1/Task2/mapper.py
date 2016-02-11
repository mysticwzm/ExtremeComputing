#!/usr/bin/python

import sys

#input from standard input
for line in sys.stdin:
    #remove the whitespace in line
    line = line.strip()
    #output the line
    print '%s\t%s' % (line,1)
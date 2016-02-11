#!/usr/bin/python
import sys

#input from standard input
for line in sys.stdin:
    # strip and turn to the lowercase
    line = line.strip().lower()
    # print the string in lowercase
    print '%s' % (line)
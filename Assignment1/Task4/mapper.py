#!/usr/bin/python

import sys

#input from standard input
for line in sys.stdin:
    #split the word into a list of word
    tokens = line.strip().split()
    #sequence can be made from the 1st index of list
    #to the len(list)-2'th index
    for i in range(0,len(tokens) - 2):
        sequences = tokens[i] + ' ' + tokens[i+1] + ' ' + tokens[i+2]
        #output the sequence as key to reducer with value 1
        print "%s\t%s" % (sequences,1)
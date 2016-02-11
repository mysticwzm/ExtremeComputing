#!/usr/bin/python

import sys
from operator import itemgetter

#the prev line
prevWord = " "
#input from STDIN
for line in sys.stdin:
    word,value = line.split('\t',1)
    #if current line equals to prev line, continue loop
    if prevWord == word:
        continue
    else:
        #else if current line does not equal to prev line
        #prevline = currnet line
        prevWord = word
        #once line changes, output new line
        print '%s' % (prevWord)
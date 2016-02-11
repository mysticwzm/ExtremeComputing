#!/usr/bin/python

import sys
from operator import itemgetter

#dictionary used to store the times of appearance in all documents for a word
d = {}
#get the word,which document it is from and the times of appearance
preTerm,file_name,value = sys.stdin.readline().strip().split('\t')
value = int(value)
#put the time of appearance into the dictionary
if file_name in d:
    d[file_name] = d[file_name] + value
else:
    d.update({file_name:value})
for line in sys.stdin:
    #get the word,which document it is from and the times of appearance
    term,file_name,value = line.strip().split('\t')
    value = int(value)
    #put the time of appearance into the dictionary
    if preTerm == term:
        if file_name in d:
            d[file_name] = d[file_name] + value
        else:
            d.update({file_name:value})
    #output the details of current word
    else:
        printString = preTerm + ' : ' + str(len(d)) + ' : {'
        for i in range(0,18):
            key = 'd' + str(i) + '.txt'
            if key in d:
                printString = printString + '(' + key + ', ' + str(d[key]) + '), '
        printString = printString[:-2] + '}'
        print printString
        #start the statistics for the new word
        preTerm = term
        d.clear()
        d.update({file_name:value})
#output the details of the last word
printString = preTerm + ' : ' + str(len(d)) + ' : {'
for i in range(0,18):
    key = 'd' + str(i) + '.txt'
    if key in d:
        printString = printString + '(' + key + ', ' + str(d[key]) + '), '
printString = printString[:-2] + '}'
print printString
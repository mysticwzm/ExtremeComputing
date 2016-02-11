#!/usr/bin/python

import sys
from operator import itemgetter

marks = ""
prevKey,prevValue = sys.stdin.readline().strip().split('\t',1)
#if there is ',' in value, it is a mark of student
if prevValue.find(',') > -1:
    #if there is '>' in marks string
    #it means this mark is not the first mark of this student
    if marks.find('>') > -1:
        marks = marks + prevValue
    else:
    #else it is the first mark of this student
    #we should add a string of " --> " before the mark
        marks = marks + " --> " + prevValue
else:
#else there is no ',' in value, this value is a name of student
    marks = prevValue + marks

for line in sys.stdin:
    key,value = line.strip().split('\t',1)
    #same student, do the judgement as before
    if prevKey == key:
        if value.find(',') > -1:
            if marks.find('>') > -1:
                marks = marks + value
            else:
                marks = marks + " --> " + value
        else:
            marks = value + marks
    else:
    #it is another student, print the name and mark(s) of former student
    #clear the string marks to store the information of new student
    #and do the judgement as before again
        print marks
        marks = ""
        prevKey = key
        if value.find(',') > -1:
            if marks.find('>') > -1:
                marks = marks + value
            else:
                marks = marks + " --> " + value
        else:
            marks = value + marks
#output the information of last student
print marks
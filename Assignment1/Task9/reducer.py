#!/usr/bin/python

import sys
from operator import itemgetter

#total mark, number of subject, maximum average
total = 0
subject = 0
max = 0
prevKey,prevValue = sys.stdin.readline().strip().split('\t',1)
#namelist to store the student(s) has/have maximum average
namelist = ""
#name of student
name = ""
if prevValue.find(',') > -1:
#if there is ',' in value, it means it is a mark of student
#add the mark to the total mark and increase number of subject by 1
    lesson,mark = prevValue.strip().split(',',1)
    mark = int(mark)
    subject = subject + 1
    total = total + mark
else:
#else there is no ',' in value, it means it is a name of student
    name = prevValue

for line in sys.stdin:
    key,value = line.strip().split('\t',1)
    #same student, do the judgement of "name or mark" as before
    if prevKey == key:
        if value.find(',') > -1:
            lesson,mark = value.strip().split(',',1)
            mark = int(mark)
            subject = subject + 1
            total = total + mark
        else:
            name = value
    else:
    #a new student,if the former student's subjects is more than 3
        if subject > 4:
            #calculate the average score
            average = total / subject
            #if average is bigger than max average
            #clear the namelist and store this student
            if average > max:
                max = average
                namelist = name + " "
            else:
                #if it is equal, add the name to the namelist
                if average == max:
                    namelist = namelist + name + " "
        #change key as the new student and clear subject,total
        prevKey = key
        subject = 0
        total = 0
        #do the judgement of "name or mark" again
        if value.find(',') > -1:
            lesson,mark = value.strip().split(',',1)
            mark = int(mark)
            subject = subject + 1
            total = total + mark
        else:
            name = value
#check the last student
if subject > 4:
    average = total / subject
    if average > max:
        max = average
        namelist = name + " "
    else:
        if average == max:
            namelist = namelist + name + " "
print namelist
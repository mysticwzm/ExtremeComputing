#!/usr/bin/python

import sys,datetime
from operator import itemgetter

preSite,time = sys.stdin.readline().strip().split('\t')
#the last visited time
time_last = datetime.datetime.strptime(time,'%d/%b/%Y:%H:%M:%S')
#the first visited time
time_first = time_last
#number of visited times
count = 1
for line in sys.stdin:
    site,time = line.strip().split('\t')
    time_temp = datetime.datetime.strptime(time,'%d/%b/%Y:%H:%M:%S')
    if preSite == site:
        #if the current time is later than the last visited time,update
        if time_temp > time_last:
            time_last = time_temp
        #if the current time is earlier than the first visited time,update
        if time_temp < time_first:
            time_first = time_temp
        #number of visited times added by 1
        count = count + 1
    else:
        #output the time difference
        if time_first != time_last:
            print '%s\t%s' % (preSite,time_last - time_first)
        else:
            #if this host just has been visited once, then output the timestamp when it was visited
            if count == 1:
                print '%s\t%s' % (preSite,time_first)
            #or output the time difference,although this host has been visited more than once
            #but all visits are in a same time
            else:
                print '%s\t%s' % (preSite,time_last - time_first)
        #start the statistics for the new host
        preSite = site
        time_last = time_temp
        time_first = time_temp
        count = 1
#output the time difference or timestamp of the last host
if time_first != time_last:
    print '%s\t%s' % (preSite,time_last - time_first)
else:
    if count == 1:
        print '%s\t%s' % (preSite,time_first)
    else:
        print '%s\t%s' % (preSite,time_last - time_first)
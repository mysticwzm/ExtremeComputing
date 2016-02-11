#!/usr/bin/python

import sys

for line in sys.stdin:
    #emit the name of host and the visited time
    time = line.strip().split(' - - ')[1].split(']')[0].split(' ')[0][1:]
    site = line.strip().split(' - - ')[0]
    if len(time) == 20:
        print '%s\t%s' % (site,time)
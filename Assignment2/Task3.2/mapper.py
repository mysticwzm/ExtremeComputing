#!/usr/bin/python

import sys

#dictionary used as an in-mapper combiner
d = {}
for line in sys.stdin:
    reply = line.strip().split('"')[-1].strip().split()[0]
    #find the log record with 404 reply
    if reply == '404':
        #get the name of host
        site = line.strip().split(' - - ')[0]
        #put this host into dictionary
        if site in d:
            d[site] = d[site] + 1
        else:
            d.update({site:1})
        # when the size of dictionary is up to 100, output all elements in it and clear itself
        # so that the memory won't be used up
        if len(d) == 100:
            for key in d:
                print '%s\t%s' % (key,d[key])
            d.clear()
#output the elements which are still in the dictionary
for key in d:
    print '%s\t%s' % (key,d[key])
d.clear()
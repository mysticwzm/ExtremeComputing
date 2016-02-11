#!/usr/bin/python

import sys

#dictionary used as an in-mapper combiner
d = {}
for line in sys.stdin:
    #get the name of page
    request = line.strip().split('"')[1]
    if len(request.split()) == 3:
        page = request.split()[1]
        #put this page into dictionary
        if page in d:
            d[page] = d[page] + 1
        else:
            d.update({page:1})
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
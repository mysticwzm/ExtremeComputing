#!/usr/bin/python

import sys,re,os

#get the name of current file
file_name = os.environ['map_input_file'].strip().split('/')[-1]
#dictionary used as an in-mapper combiner
d = {}
for line in sys.stdin:
    line = line.strip()
    #just extract the words purely consist of upper&lower characters
    tokens = re.findall('[A-Za-z]+',line)
    #put the extracted words into dictionary
    for token in tokens:
        if token in d:
            d[token] = d[token] + 1
        else:
            d.update({token:1})
        # when the size of dictionary is up to 100, output all elements in it and clear itself
        # so that the memory won't be used up
        if len(d) == 100:
            for key in d:
                print '%s\t%s' % (key,file_name + '\t' + str(d[key]))
            d.clear()
#output the elements which are still in dictionary
if len(d) > 0:
    for key in d:
        print '%s\t%s' % (key,file_name + '\t' + str(d[key]))
    d.clear()
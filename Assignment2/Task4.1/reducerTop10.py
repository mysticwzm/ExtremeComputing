#!/usr/bin/python

import sys
from operator import itemgetter

index = 0
for line in sys.stdin:
    #output the top 10 ids of question and numbers of viewcount
    if index < 10:
        index = index + 1
        viewCount,questionId = line.strip().split('\t',1)
        #999999999 minus the number of viewcount again to restore the original number of viewcount
        viewCount = 999999999 - int(viewCount)
        print '%s\t%s' % (questionId + ',\t',viewCount)
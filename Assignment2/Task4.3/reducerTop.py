#!/usr/bin/python

import sys
from operator import itemgetter

maxCount = 0
maxOwnerUserId = ''
maxAnswerIds = ''
for line in sys.stdin:
    OwnerUserId,AnswerIds = line.strip().split('\t',1)
    count = len(AnswerIds.split(','))
    #find the owneruserid which has the biggest number of answers from 10 candidates
    if count > maxCount:
        maxCount = count
        maxOwnerUserId = OwnerUserId
        maxAnswerIds = AnswerIds
#output the final result
print maxOwnerUserId + '\t->\t' + str(maxCount) + ',\t' + maxAnswerIds
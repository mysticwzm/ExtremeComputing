#!/usr/bin/python

import sys
from operator import itemgetter

preOwnerUserId,preAnswerId = sys.stdin.readline().strip().split('\t')
count = 1
AnswerIds = preAnswerId
maxCount = 0
maxAnswerIds = ''
maxOwnerUserId = ''
for line in sys.stdin:
    OwnerUserId,AnswerId = line.strip().split('\t')
    #mix all ids of answer of the same owneruserid
    if OwnerUserId == preOwnerUserId:
        count = count + 1
        AnswerIds = AnswerIds + ', ' + AnswerId
    #compare the number of answers with the maximum number of answer
    #if it is bigger than that, update 
    else:
        if count > maxCount:
            maxCount = count
            maxAnswerIds = AnswerIds
            maxOwnerUserId = preOwnerUserId
    #start the statistics for the new owneruserid
        count = 1
        AnswerIds = AnswerId
        preOwnerUserId = OwnerUserId
#comparison of the last owneruserid
if count > maxCount:
    maxCount = count
    maxAnswerIds = AnswerIds
    maxOwnerUserId = preOwnerUserId
#output the owneruserid which has the biggest number of answers
print '%s\t%s' % (maxOwnerUserId,maxAnswerIds)
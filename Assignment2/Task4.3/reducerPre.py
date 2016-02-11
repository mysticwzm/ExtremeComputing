#!/usr/bin/python

import sys
from operator import itemgetter

preAnswerId,CurrentOwnerUserId = sys.stdin.readline().strip().split('\t')
OwnerUserId = CurrentOwnerUserId
count = 1
for line in sys.stdin:
    AnswerId,CurrentOwnerUserId = line.strip().split('\t')
    #if the answerid is the same, update the owneruserid if the current owneruserid is not 0
    if AnswerId == preAnswerId:
        count = count + 1
        if CurrentOwnerUserId != '0':
            OwnerUserId = CurrentOwnerUserId
    else:
        #if we have find a pair of question and accepted answer, then output the owneruserid of this answer and id of this answer
        if count > 1:
            print '%s\t%s' % (OwnerUserId,preAnswerId)
        count = 1
        preAnswerId = AnswerId
        OwnerUserId = CurrentOwnerUserId
if count > 1:
    print '%s\t%s' % (OwnerUserId,preAnswerId)
#!/usr/bin/python

import sys
from operator import itemgetter

maxCount = 0
maxOwnerUserId = ''
maxPostIds = ''
for line in sys.stdin:
    OwnerUserId,PostIds = line.strip().split('\t',1)
    parts = len(PostIds.strip().split())
    #find the owneruserid which has maximum number of answers among 10 ownerusersids
    if parts > maxCount:
        maxOwnerUserId = OwnerUserId
        maxPostIds = PostIds
        maxCount = parts
#output the final result
print maxOwnerUserId + '\t->\t' + maxPostIds  
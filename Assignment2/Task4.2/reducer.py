#!/usr/bin/python

import sys
from operator import itemgetter

preOwnerUserId, prePostId = sys.stdin.readline().strip().split('\t',1)
count = 1
PostIds = prePostId
maxCount = 1
maxOwnerUserId = preOwnerUserId
maxPostIds = prePostId
for line in sys.stdin:
    OwnerUserId,PostId = line.strip().split('\t',1)
    #if it is the same owneruserid, add the number of answers by 1
    #and update the string of postids
    if preOwnerUserId == OwnerUserId:
        count = count + 1
        PostIds = PostIds + ', ' + PostId
    #if the number of answers of this owneruserid, update all maximum variables
    else:
        if count > maxCount:
            maxCount = count
            maxOwnerUserId = preOwnerUserId
            maxPostIds = PostIds
        preOwnerUserId = OwnerUserId
        count = 1
        PostIds = PostId
#compare the number of answers of last owneruserid
if count > maxCount:
    maxCount = count
    maxOwnerUserId = preOwnerUserId
    maxPostIds = PostIds
#output the owneruserid with maximum number of answers and its string of postids
print '%s\t%s' % (maxOwnerUserId,maxPostIds)
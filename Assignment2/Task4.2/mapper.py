#!/usr/bin/python

import sys

questionType = 'PostTypeId="2"'
for line in sys.stdin:
    if questionType in line:
        if 'OwnerUserId' in line and 'ParentId' in line:
            #get the owneruserid and the id of question this answer applied to
            OwnerUserId = line.strip().split('OwnerUserId="',1)[1].split('"',1)[0]
            PostId = line.strip().split('ParentId="',1)[1].split('"',1)[0]
            print '%s\t%s' % (OwnerUserId,PostId)
#!/usr/bin/python

import sys

questionType1 = 'PostTypeId="1"'
questionType2 = 'PostTypeId="2"'

for line in sys.stdin:
    #if this log record is a question, then emit its acceptedanswerid
    if questionType1 in line:
        if 'AcceptedAnswerId' in line:
            AcceptedAnswerId = line.strip().split('AcceptedAnswerId="',1)[1].split('"',1)[0]
            print '%s\t%s' % (AcceptedAnswerId,0)
    #if this log record is a answer, then emit its id and owneruserid
    if questionType2 in line:
        if 'Id' in line and 'OwnerUserId' in line:
            AnswerId = line.strip().split('Id="',1)[1].split('"',1)[0]
            OwnerUserId = line.strip().split('OwnerUserId="',1)[1].split('"',1)[0]
            print '%s\t%s' % (AnswerId,OwnerUserId)
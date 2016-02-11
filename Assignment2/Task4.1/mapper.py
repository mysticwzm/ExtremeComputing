#!/usr/bin/python

import sys

questionType = 'PostTypeId="1"'
for line in sys.stdin:
    if questionType in line:
        if 'ViewCount' in line and 'Id' in line:
            #get the number of viewcount and id of question
            viewCount = line.strip().split('ViewCount="',1)[1].split('"',1)[0]
            questionId = line.strip().split('Id="',1)[1].split('"',1)[0]
            #in order to sort from high to low, I use 999999999 which is a 'big' number
            #to minus the number of viewcount of each log
            #the bigger the number of viewcount is, the smaller result got after the minus
            viewCount = 999999999 - int(viewCount)
            print "%s\t%s" % (viewCount,questionId)
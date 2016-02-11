#!/usr/bin/python

import sys
from operator import itemgetter

index = 0
for line in sys.stdin:
    #output the top 10 numbers of viewcount and ids of question
    if index < 10:
        index = index + 1
        print line.strip()
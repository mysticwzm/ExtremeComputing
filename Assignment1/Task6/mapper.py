#!/usr/bin/python

import sys

#input from standard input
#the input file is the output file of task5
for line in sys.stdin:
    value,key = line.strip().split('\t',1)
    #in order to make number of sequence sorted from high to low
    #use the result of 999999999 minus this number of sequence as key
    #because the key will be sorted in string type
    key = 9999999999 - int(key)
    #output key and value
    print '%s\t%s' % (key,value)

#about 999999999:
#the webLarge.txt has 123588873 words
#therefore, it has 123588871 sequences at most
#if we output the number of sequence as key to reducer
#it will be sorted as "1","12","2", which is in "string order", from low to high
#however, what I want is a order from high to low and get the top20 number
#So I use 999999999 as a "big" number to minus every number of sequence 
#after that, all numbers will be in same length, which is 9bits
#the bigger number will have less 9 at the start
#while the smaller number will have more 9
#in terms of the numbers except 9, which is "real number"
#bigger the number is, smaller the (9-this number) is
#for example, 7 is bigger than 6, but (9-7) is smaller than (9-6)
#so I use the result of 999999999 minus this number as key 
#these keys will be sort from low to high in "string order"
#which actually means the original numbers sorted from high to low
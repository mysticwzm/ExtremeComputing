#!/usr/bin/python

import sys

#input from STDIN
for line in sys.stdin:
    #the first number in line is the number of row
    #which is split by '\t'
    row,array = line.strip().split('\t',1)
    #the following numbers are numbers in matrix
    numbers = array.split()
    #col is used to record the number of column
    col = 0
    for number in numbers:
        if number:
            colString = str(col)
            key = "0" * (4-len(colString)) + colString + "0" * (4-len(row)) + row
            value = number
            col = col + 1
            print '%s\t%s' % (key,value)

#after the transpose, row becomes column and column becomes to row
#as the matrixLarge is 4000*3000, I create a series in 8bits
#first 4bits means row and the following 4bits means column after transpose
#for instance,(1,10)=(000)1(00)10 and (100,1000)=(0)100()1000
#which means if the length of number is smaller than 4bits
#I will use sufficient numer of 0 to replenish the number to be 4bits
#and then this series can be sorted by hadoop in "string order"
#and the result is precisely equal to the result which is 
#firstly sort by row and for same row sort by column
#!/usr/bin/python

import sys

#the set to store the words from terms.txt
dic = set()
d = 'd1.txt'
#add all words in terms.txt to the set
for line in file('terms.txt'):
    line = line.strip()
    dic.add(line)
for line in sys.stdin:
    word,idf,tf = line.strip().split(' : ')
    #when the current word is a word in the set
    if word in dic:
        #and this word appears in d1.txt
        if d in tf:
            #output its value of tf and idf, and remove this word from set
            tf = tf.strip().split(', ',1)[1].split(')',1)[0]
            print '%s\t%s' % (word,tf + '\t' + idf)
            dic.remove(word)
#if there are any words reamaining in the set, then output its tf and idf as 0 and 0
#because these words do not appear in d1.txt and its score should be 0 
for word in dic:
    print ('%s\t%s' % (word,'0\t0'))
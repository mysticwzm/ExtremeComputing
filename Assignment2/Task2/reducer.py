#!/usr/bin/python

import sys,math
from operator import itemgetter

#two dictionaries to store the tfs and idfs
d_tf = {}
d_idf = {}
for line in sys.stdin:
    #get the word and its value of tf&idf from mapper
    word,values = line.strip().split('\t',1)
    tf,idf = values.strip().split('\t')
    tf = float(tf)
    idf = float(idf)
    #put the value of tf&idf into dictionaries
    if word in d_tf:
        d_tf[word] = d_tf[word] + tf
        d_idf[word] = d_idf[word] +idf
    else:
        d_tf.update({word:tf})
        d_idf.update({word:idf})
#output the scores
for word in d_tf:
    score = str(d_tf[word] * math.log10(17 / (1 + d_idf[word])))
    print '%s' % (word + ', d1.txt = ' + score)
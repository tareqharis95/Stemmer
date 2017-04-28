#!/usr/bin/env python

import sys
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

stopWords = set(stopwords.words('english'))
ps = PorterStemmer()

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    words = word_tokenize(line)
    for word in words:
                
        if word not in stopWords:
        print '%s\t%s' % (ps.stem(word), 1)
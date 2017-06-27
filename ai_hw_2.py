###
# This is for using in ipython(not important)

# coding: utf-8
#get_ipython().magic('load ai_hw_1.py')
# %load ai_hw_1.py

###

###
# you can import this file in jupyter with
# load ai_hw_2.py OR
# from ai_hw_2 import *
###
from nltk.book import *
#text1
from nltk.corpus import gutenberg
gutenberg.fileids()

# load book from gutenberg
emma = gutenberg.words('austen-sense.txt')
emma
gutenberg.fileids()

# Number of sentences
#num_sents = len(gutenberg.sents('austen-emma.txt'))
#print('Number of sentences:',num_sents)

# sentences is a list of sentences in the book
sentences = gutenberg.sents('chesterton-ball.txt')
sentences
# Number of sentences in the book
len(sentences)
sent_len = []
    
#for line in range(0, len(sentences)):
#    sent_len = len(sentences [line])
    
# number of sentences    
#sent_len
#len(sentences)

# range from 0 to no. of sentences
#range(0, len(sentences))
    
    
    
#sent_len = []

# type of sent_len is list
type(sent_len)

# trying to append numbers to sent_len
#sent_len.append(1)
#sent_len.append(2)


#type(line)
#sent_len = []
#sent_len
#line
#sentences
#line
#sent_len
#sentences[0]
#len(sentences[0])
#new = []
#new.append(len(sentences[0]))
#new.append(len(sentences[1]))
#new
#line
#sent_len

# Adding length of each sentence to the sent_len list
for line in range(0, len(sentences)):
    sent_len.append(len(sentences[line]))
    
sent_len

# Longest sentence
max(sent_len)

# Finding the longest sentence by its index
import numpy as np
ind = np.argmax(sent_len)
# index of the longest sentence
ind
sentences[ind]

# grouping sentences of similar length
from collections import Counter
occurences = Counter(sent_len)
occurences
#get_ipython().magic('save ai_hw_1 1-61')
#ipython -i [filename]
#sent_len
# arranging list of 'sentence lenths' in ascending order
sort_sent_len = sorted(sent_len)
sort_sent_len
#sent_len
#sort_sent_len

# now grouping sentences of similar length in ascending order
sort_occ = Counter(sort_sent_len)
sort_occ

# for plotting the histogram of grouped sentence lengths in ascending order
import numpy as np
import matplotlib.pyplot as plt
labels, values = zip(*sort_occ.items())
indexes = np.arange(len(labels))
width = 0.5
plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels)
plt.tight_layout()
plt.show()
#https://stackoverflow.com/questions/19198920/using-counter-in-python-to-build-histogram

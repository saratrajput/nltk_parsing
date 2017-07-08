# coding: utf-8
#get_ipython().magic('load ai_hw_2.py')
# %load ai_hw_2.py
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
#gutenberg.fileids()



# sentences is a list of sentences in the book
sentences = gutenberg.sents('chesterton-ball.txt')
sentences
# Number of sentences in the book
len(sentences)

# empty list to store lenght of each sentence as a list
sent_len = []
    

# type of sent_len is list
type(sent_len)


# Adding length of each sentence to the sent_len list
for line in range(0, len(sentences)):
    sent_len.append(len(sentences[line]))

# checking sent_len     
sent_len

# length of Longest sentence
max(sent_len)

# Finding the longest sentence by its index
import numpy as np
ind = np.argmax(sent_len)
# index of the longest sentence
ind
# longest sentence
sentences[ind]

# grouping sentences of similar length
from collections import Counter
occurences = Counter(sent_len)
occurences
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
#plt.show()
#https://stackoverflow.com/questions/19198920/using-counter-in-python-to-build-histogram

## Pos tagging
len(sentences[ind])

import nltk
from nltk import load_parser
from nltk import pos_tag, word_tokenize, CFG
for i in parser.parse(testsentence):
    print i
for i in parser.parse(testsentence):
    print(i)
    break
testsentence
testy = ['show', 'me', 'northwest', 'flights', 'to', 'detroit', '.']
for i in parser.parse(testy):
    print(i)
    break
sentences[ind]
sentences[10]
type(sentences[10])
testy = ['show', 'me', 'northwest', 'flights', 'to', 'detroit', '.']
type(testy)
testy_new = ['That','object','which','seemed','to','be','created','by','the','entanglement','of','two','corkscrews','was','really','the','key','.']
for i in parser.parse(testy_new):
    print(i)
    break
for i in parser.parse(testy):
    print(i)
    break
testy = ['show', 'me','that', 'northwest', 'flights', 'to', 'detroit', '.']
for i in parser.parse(testy):
    print(i)
    break
testy = ['show', 'me', 'northwest', 'flights', 'to', 'detroit', '.']
for i in parser.parse(testy):
    print(i)
    break
testy_new = ['that','object','which','seemed','to','be','created','by','the','entanglement','of','two','corkscrews','was','really','the','key','.']
for i in parser.parse(testy_new):
    print(i)
    break
testy = ['show', 'me', 'northwest', 'objects', 'to', 'detroit', '.']
for i in parser.parse(testy):
    print(i)
    break
sentences[ind]
[x.lower() for x in sentences[ind]]
tamarah = [x.lower() for x in sentences[ind]]

tamarah
tam_string = ' '.join(tamarah)
tam_string
tag_tam = nltk.word_tokenize(tam_string)
list_of_tokesn = nltk.pos_tag(tag_tam)

########################################

# load atis grammar from large grammar

grammar = nltk.data.load('grammars/large_grammars/atis.cfg')

# to use Top Down Chart Parser with large grammar
parser = nltk.TopDownChartParser(grammar, trace = 2)
for tree in parser.parse(test_sent):
    print(tree)

# simple grammar    
grammar1 = nltk.CFG.fromstring("""
    S -> NP VP
    VP -> V NP | V NP PP
    PP -> P NP
    V -> 'saw' | 'ate' | 'walked'
    NP -> 'Jonh' | 'Mary' | 'Bob' | Det N | Det N PP
    Det -> 'a' | 'an' | 'the' | 'my'
    N -> 'man' | 'dog' | 'cat' | 'telescope' | 'park'
    P -> 'in' | 'on' | 'by' | 'with'
""")

# to use Top Down Chart Parser with simple grammar
parser = nltk.TopDownChartParser(grammar1, trace = 2)
   
# load test sent with all lower characters 
test_sent = [x.lower() for x in sentences[ind]]
test_sent

# test parser
for tree in parser.parse(test_sent):
    print(tree)


# error: input words missing    
#parser = nltk.TopDownChartParser(grammar, trace = 2)
#for tree in parser.parse(test_sent):
#    print(tree)
    
    

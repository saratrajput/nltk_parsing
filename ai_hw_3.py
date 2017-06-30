# coding: utf-8
get_ipython().magic('load ai_hw_2.py')
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

## Large grammar
len(sentences[ind])
my_grammar = nltk.data.load('grammars/large_grammars/atis.cfg')
import nltk
my_grammar = nltk.data.load('grammars/large_grammars/atis.cfg')
my_grammar
test_sent = sentences[ind]
test_sent
my_parser = ChartParser(my_grammar)
from nltk import load_parser
my_parser = ChartParser(my_grammar)
from nltk import pos_tag, word_tokenize, CFG
my_parser = ChartParser(my_grammar)
my_parser = nltk.ChartParser(my_grammar)
my_sent
test_sent
for i in my_parser.parse(test_sent):
    print 8
for i in my_parser.parse(test_sent):
    print(i)
    break
test_sent1 = "The sun rises in the east."
for i in my_parser.parse(test_sent1):
    print(i)
    break
parser
my_parser
chart = my_parser.parse(test_sent)
print((chart.num_edges()))
chart
chart = my_parser.parse(test_sent)
parser = nltk.parse.BottomUpChartParser(grammar)
grammar
my_grammar
parser = nltk.parse.BottomUpChartParser(my_grammar)
chart = parser.chart_parse(test_sent)
parser = nltk.parse.LeftCornerChartParser(my_grammar)
chart = parser.chart_parse(test_sent)
parser = nltk.parse.TopDownChartParser(my_grammar)
chart = parser.chart_parse(test_sent)
parser = nltk.parse.TopDownChartParser(my_grammar)
chart = parser.chart_parse(test_sent1)
new_sentences = nltk.data.load('grammars/large_grammars/atis_sentences.txt')
new_sentences = nltk.parse.util.extract_test_sentences(new_sentences)
len(new_sentences)
testsentence = new_sentences[22]
testsentences[0]
testsentence[0]
new_sentence = testsentence[0]
parser = nltk.parse.BottomUpChartParser(my_grammar)
chart = parse.chart_parse(new_sentence)
chart = parser.chart_parse(new_sentence)
print((len(list(chart.parses(grammar.start())))))
print((len(list(chart.parses(my_grammar.start())))))
parser
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
for i in parser.parse(tamarah):
    print(i)
    break
tamarah
tam_string = ' '.join(tamarah)
tam_string
tag_tam = nltk.word_tokenize(tam_string)
nltk.pos_tag(tag_tam)
get_ipython().magic('save ai_hw_3.py 1-82')

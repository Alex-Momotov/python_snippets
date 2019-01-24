import nltk
import os
os.chdir(r'C:\Users\Sasha\Coding\Python\0. Learning Python\9. nltk_')

#%% Import some text to work with
import pickle
with open(r'C:\Users\Sasha\Coding\Python\4. Dissertation\Processing '
          r'Stages\3. Missing Arts Deleted/2010-01-01.pickle', 'rb') as f:
    text = pickle.load(f)
text = text[2]['body']

#%%
"""
Named Entity Types:

ORGANISAION     Georgia-Pacific Corp., WHO
PERSON          Eddy Bonte, President Obama
LOCATION        Murray River, Mount Everest
DATE            June, 2008-06-29
TIME            two fifty a m, 1:30 p.m.
MONEY           175 million Canadian Dollars, GBP 10.40
PERCENT         twenty pct, 18.75 %
FACILITY        Washingtom Monument, Stonehenge
GPE             South East Asia, Midlothian
"""
#%% nltk.ne_chunk(POS_tagged_sent, binary=False)
#   Takes in a POS tagged sentence (list of tuples) and returns a tree with identified named entities.
#   Setting binary=True will label all entities as NE instead of specific NE tags, sometimes thats more accurate.
#   False positive of NLTK's NER algorithm is quite high, we can always use chuncking and looking for nouns to do NER.
from nltk import sent_tokenize
from nltk import word_tokenize
sentences = sent_tokenize(text)
sentences_tokened = [word_tokenize(sent) for sent in sentences]
sentences_tagged = nltk.pos_tag_sents(sentences_tokened)
sentences_NER = [nltk.ne_chunk(sent_t, binary=True) for sent_t in sentences_tagged]
sentences_NER[0].draw()

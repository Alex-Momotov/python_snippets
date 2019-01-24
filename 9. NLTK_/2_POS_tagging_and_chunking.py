import nltk
import os
os.chdir(r'C:\Users\Sasha\Coding\Python\0. Learning Python\9. nltk_')

#%% Import some text to work with
import pickle
with open(r'C:\Users\Sasha\Coding\Python\4. Dissertation\Processing '
          r'Stages\3. Missing Arts Deleted/2010-01-01.pickle', 'rb') as f:
    text = pickle.load(f)
text = text[2]['body']

#%% nltk.pos_tag(list_of_sent_words, tagset=None)
#   Takes in a list of words from a single sentence. Returns list of tuples where each word is tagged as part of speech.
#   By default uses NLTK's recommended tagset, but we can specify a simpler tagset using: tagset='universal'
#   We must call nltk.pos_tag on a list of tokens for each individual sentence, not across many sentences.
#   The idea is to create a list of sentences where each sentence is a list of tuples of (word, part of speech)
from nltk import sent_tokenize
from nltk import word_tokenize
sentences = sent_tokenize(text)
sentences_tokened = [word_tokenize(sent) for sent in sentences]
sentences_tagged = [nltk.pos_tag(words_in_sent) for words_in_sent in sentences_tokened]
for sent in sentences_tagged: print(sent,'\n')

#%% Using universal tagset instead (simpler)
sentences_tagged = [nltk.pos_tag(words_in_sent, tagset='universal') for words_in_sent in sentences_tokened]
for sent in sentences_tagged: print(sent,'\n')

#%% nltk.pos_tag_sents(sentences, tagset=None)
#   Part-of-speech tags a given list of sentences, each consisting of a list of tokens.
#   A more efficient way to tag more than one sentence.
from nltk import sent_tokenize
from nltk import word_tokenize
sentences = sent_tokenize(text)
sentences_tokened = [word_tokenize(sent) for sent in sentences]
sentences_tagged = nltk.pos_tag_sents(sentences_tokened, tagset='universal')
for sent in sentences_tagged: print(sent,'\n')

#%%
""" 
Part of Speech Tag list:
CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent's
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when
"""
#%% nltk.RegexpParser(grammar, , root_label='S')
#   Returns a chunk parser object which uses the provided grammar. Root label is self explanatoty.
#   The grammar should be a string which uses POS tags and regular expressions to define a chunk.
#   See this page for how to define your own grammar rules: https://www.nltk.org/api/nltk.chunk.html?highlight=nltk%20regexpparser#nltk.chunk.regexp.RegexpParser
#   chunkParser.parse(chunk_struct)
#   Takes in a single POS tagged tokenised sentence and returns a tree of chunks.

#   This is the code we know from before
from nltk import sent_tokenize
from nltk import word_tokenize
sentences = sent_tokenize(text)
sentences_tokened = [word_tokenize(sent) for sent in sentences]
sentences_tagged = nltk.pos_tag_sents(sentences_tokened)

#   Here we define our chunk and create chunk parser
grammar = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
chunkParser = nltk.RegexpParser(grammar, root_label='Root')

sentences_chunked = [chunkParser.parse(sent_t) for sent_t in sentences_tagged]
for sent in sentences_chunked: print(sent,'\n\n')
sentences_chunked[-1].draw()

#%%     ### Chinking ###
#   Chinking is when we specify which things we want to keep out of our chunk.
#   This is done by writing grammar expressions between close and open curly braces }{
grammar = r"""Chunk: {<.*>+}
                            }<VB.?|IN|DT|TO>+{"""
chunkParser = nltk.RegexpParser(grammar, root_label='Root')

sentences_chunked = [chunkParser.parse(sent_t) for sent_t in sentences_tagged]
for sent in sentences_chunked: print(sent,'\n\n')
sentences_chunked[0].draw()







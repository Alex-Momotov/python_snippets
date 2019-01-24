import nltk
import os
os.chdir(r'C:\Users\Sasha\Coding\Python\0. Learning Python\9. nltk_')

#%% Import some text to work with
import pickle
with open(r'C:\Users\Sasha\Coding\Python\4. Dissertation\Processing '
          r'Stages\3. Missing Arts Deleted/2010-01-01.pickle', 'rb') as f:
    data = pickle.load(f)
text = data[2]['body']

#%% sent_tokenize(text, language='english')
#   Return a sentence-tokenized copy of text, as a list of sentences.
from nltk import sent_tokenize
sentences = sent_tokenize(text)
for sent in sentences: print(sent, '\n')

#%% tokenizer = PunktSentenceTokenizer()
#   tokenizer.tokenize(text)
#   Another sentence tokenizer. Uses unsupervised learning. Comes already pretrained. Returns a list of sentences.
#   We could train the tokenizer further by passing: tokenizer = PunktSentenceTokenizer(training_text)
from nltk import PunktSentenceTokenizer
tokenizer = PunktSentenceTokenizer(data[3]['body'])
tokened_text = tokenizer.tokenize(data[2]['body'])
for sent in tokened_text: print(sent, '\n')

#%% word_tokenize(text, language='english', preserve_line=False)
#   Return a tokenized copy of text, as a list of words.
from nltk import word_tokenize
tokened_text = word_tokenize(text)
for word in tokened_text: print(word)

#%% stopwords.words('english')
#   Returns a list of English stopwords.
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
print(stop_words)
print(len(stop_words))

#   Most probably you want to make a set out of these, for faster lookup
stop_words = set(stopwords.words('english'))

#%%
#   You can easily add your own stop words to the set, for example, by making a
#   Counter() of all words in corpus and removing e.g. 20 most frequent ones.

#   A one line code to remove stop words from a text:
#   Note we use .lower() only during checking for stop_words
tokened_text = word_tokenize(text)
filtered_text = [wrd for wrd in tokened_text if wrd.lower() not in stop_words]
print(filtered_text)
print(len(tokened_text), len(filtered_text))

#%% ps = PorterStemmer()
#   Returns a word stemmer based on the Porter Stemming algorithm.
#   ps.stem(word)
#   Returns stem of a given word. All words are automatically converted to lower case.
from nltk.stem import PorterStemmer
ps = PorterStemmer()
example_words = ['snake','snaked','snaking','snakely']
stems = [ps.stem(w) for w in example_words]
print(stems)

#%% Full script example of tokenising, removing punctuation, stop word removal and stemming a text
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk
import pickle

#   Get some text to work with
with open(r'C:\Users\Sasha\Coding\Python\4. Dissertation\Processing '
          r'Stages\3. Missing Arts Deleted/2010-01-01.pickle', 'rb') as f:
    text = pickle.load(f)
text = text[2]['body']

#   Load stop words and create Porter Stemmer
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

#   Main text processing part
tokened_text = word_tokenize(text)                                                      # Tokenization
punct_rem_text = [wrd for wrd in tokened_text if wrd.isalnum()]                         # Punctuation removal
filtered_text = [wrd for wrd in punct_rem_text if wrd.lower() not in stop_words]        # Stop word removal
stemmed_text = [ps.stem(wrd) for wrd in filtered_text]                                  # Stemming
print(stemmed_text)


#%% Import some text to work with and some housekeeping
import os
import pickle
os.chdir(r'C:\Users\Sasha\Coding\Python\0. Learning Python\9. nltk_')
with open(r'C:\Users\Sasha\Coding\Python\4. Dissertation\Processing '
          r'Stages\3. Missing Arts Deleted/2010-01-01.pickle', 'rb') as f:
    text = pickle.load(f)
text = text[2]['body']

#%% lemmatizer = WordNetLemmatizer()
#   Creates the lemmetizer object
#   lemmatizer.lemmatize(word, pos_tag=n)
#   Returns lemmetised version of the word, works best when we provide POS tag:
#   noun = n, verb = v, adjective = a, adverb = r,  s=
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("expanding"))
print(lemmatizer.lemmatize("expanding", 'v'))
print(lemmatizer.lemmatize("sweeter"))
print(lemmatizer.lemmatize("sweeter", 'a'))
print(lemmatizer.lemmatize("better"))
print(lemmatizer.lemmatize("better", 'a'))
print(lemmatizer.lemmatize("quickly"))
print(lemmatizer.lemmatize("slowly", 'v'))


#%%
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

#   Load stop words and create Porter Stemmer
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()

#   Main text processing part
word_tokens = word_tokenize(text)                                                      # Tokenization
punct_rem_text = [wrd for wrd in word_tokens if wrd.isalnum()]                         # Punctuation removal
filtered_text = [wrd for wrd in punct_rem_text if wrd.lower() not in stop_words]       # Stop word removal
lemmatized_text = [lemmatizer.lemmatize(wrd) for wrd in filtered_text]                 # Lemmatising
lemmatized_text = [lemmatizer.lemmatize(wrd, 'v') for wrd in lemmatized_text]                 # Lemmatising
lemmatized_text = [lemmatizer.lemmatize(wrd, 'a') for wrd in lemmatized_text]                 # Lemmatising
lemmatized_text = [lemmatizer.lemmatize(wrd, 'r') for wrd in lemmatized_text]                 # Lemmatising
lemmatized_text = [lemmatizer.lemmatize(wrd, 's') for wrd in lemmatized_text]                 # Lemmatising
stemmed_text = [ps.stem(wrd) for wrd in lemmatized_text]                               # Stemming
print(stemmed_text)







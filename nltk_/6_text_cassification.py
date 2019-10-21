import nltk
import random
import os
from nltk.corpus import movie_reviews
os.chdir(r'C:\Users\Sasha\Coding\Python\0. Learning Python\9. nltk_')
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2000]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

featuresets = [(document_features(d), c) for (d, c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]

# Training a classifier and printing accuracy
classifier = nltk.NaiveBayesClassifier.train(train_set)
print('Original Naive Bayes classifier accuracy:', nltk.classify.accuracy(classifier, test_set)*100)

# Print most informative features
classifier.show_most_informative_features(800)
#%% Print out some full movie review texts
fileid = movie_reviews.fileids('neg')[7]
single_movie = movie_reviews.raw(fileid)
print(single_movie)

#%% nltk.FreqDist(list_of_words)
#   Acts like a counter to count all possible words and their respective frequencies.
freq_dist = nltk.FreqDist(all_words)

#   freq_dist.most_common(x)
#   Returns a list of x most common words.
print(freq_dist.most_common(15))

#   freq_dist.plot(x, cumulative=True)
#   Plots a cumulative curve of how many samples are made up of the x most common words
freq_dist.plot(100, cumulative=True)

#   freq_dist.N()
#   Returns the total number of words (samples), which is the length of the list of words passed during initialisation.
print(freq_dist.N())

#   freq_dist.B()
#   Returns the total number of unique words ocurring in the text. Same as len(freq_dist)
print(freq_dist.B())

#   freq_dist.hapaxes()
#   Return a list of all samples that occur once.

#   freq_dist['we']
#   Similarly to the Counter type, FreqDist object can be indexed like a dictionary

#   freq_dist.freq('the')
#   Return the frequency of a given sample.  The frequency of a
#   sample is defined as the count of that sample divided by the
#   total number of sample outcomes that have been recorded by
#   this FreqDist.

#%% This is an NLTK wrapper around the sklearn classifier
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(train_set)
print('MNB_classifier accuracy:', nltk.classify.accuracy(MNB_classifier, test_set)*100)

# Print most informative features
MNB_classifier.show_most_informative_features(100)

#%%
BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(train_set)
print('BernoulliNB accuracy:', nltk.classify.accuracy(BernoulliNB_classifier, test_set)*100)

LogisticRegression, SGDClassifier
SVC, LinearSVC, NuSVC

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(train_set)
print('LogisticRegression accuracy:', nltk.classify.accuracy(LogisticRegression_classifier, test_set)*100)

SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(train_set)
print('SGDClassifier accuracy:', nltk.classify.accuracy(SGDClassifier_classifier, test_set)*100)

SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(train_set)
print('SVC accuracy:', nltk.classify.accuracy(SVC_classifier, test_set)*100)

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(train_set)
print('LinearSVC accuracy:', nltk.classify.accuracy(LinearSVC_classifier, test_set)*100)

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(train_set)
print('NuSVC accuracy:', nltk.classify.accuracy(NuSVC_classifier, test_set)*100)




















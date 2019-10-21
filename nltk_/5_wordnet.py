from nltk.corpus import wordnet

#%% wordnet.synsets(word)
#   Returns synonyms to a particular word.
#   Nonation within synset indicates part of speach and meaning number.
#   E.g. good.n.01 means noun 'good' meaning number 1.

syn_set = wordnet.synsets('good')
print(syn_set[0])

#   Get a single synonym from the list of meanings
synon = syn_set[0].lemmas()[0].name()
print(synon)

#   Get defenition of a particular synonym
definition = syn_set[0].definition()
print(definition)

#   Get an example for a particular synonym
example = syn_set[0].examples()
print(example)

#%% Make a set of all synonyms and antonyms to a particular word
syn_set = wordnet.synsets('bad')
synonyms = set()
antonyms = set()
for word in syn_set:
    for lemma in word.lemmas():
        synonyms.add(lemma.name())
        if lemma.antonyms():
            antonyms.add(lemma.antonyms()[0].name())
print(synonyms, '\n')
print(antonyms)

#%% wordnet.synset('ship.n.01')
#   Notice, previous function was synsets, not synset.
#   Returns synset for a single word.
w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')

#   w1.wup_similarity(w2)
#   Retunrs a percent similarity between two words
print(w1.wup_similarity(w2))

#%%
w1 = wordnet.synset('king.n.01')
w2 = wordnet.synset('queen.n.01')
print(w1.wup_similarity(w2))

#%%     ### SentiWordNet ###
#   swn.senti_synset('word')
#   Returns an object which tells positive, negaive and objectivity scores for a given word.
#   word.pos_score()    Returns positive score
#   word.neg_score()    Returns negative score
#   word.obj_score()    Returns objectivity score

from nltk.corpus import sentiwordnet as swn
word = swn.senti_synset('excellent.a.01')
print(word)
print('pos score', word.pos_score())
print('neg score', word.neg_score())
print('obj score', word.obj_score())






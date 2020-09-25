import pickle
import json
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords, wordnet


##Loads in records of inputs and responses
data_file = open('Resources/intents.json').read()
intents = json.loads(data_file)

##initilizaes files for NLP
ignore_words = ['?', '!', "'s", ',', 'a', 'the', 'and', 'be']
words = pickle.load(open('Resources/words.pkl', 'rb'))
classes = pickle.load(open('Resources/classes.pkl', 'rb'))

lemmatizer = WordNetLemmatizer()

def nltkTag2WordnetTag(tag):
    """Inputs a POS tag and if it is
    a Noun, Verb, Adjective, or Adverb returns
    the corresponding WordNet POS code"""
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

def cleanSentence(input):
    """Inputs input - the string input to the chatbot
    returns: the resulting list of lemmatized words and with
    ignore words filtered out"""
    print("Cleaning Sentence")
    cleanedInSen = []
    for word, tag in pos_tag(word_tokenize(input)):
        wntag = nltkTag2WordnetTag(tag)
        if not wntag: ## is the word is not on of the above parts of speech
            lemma = word.lower() ##just make it lowercase
        else:
            lemma = lemmatizer.lemmatize(word.lower(), wntag) ##lemmatize and factor in the part of speech
        if (lemma not in ignore_words):
            cleanedInSen.append(lemma)
    return cleanedInSen

def makeBag(cleanedInSen):
    """Inputs in a list of cleaned words and checks to see if they are in the NN input words
    Returns: a numpy array of inputs to the NN"""
    print("Making Bag of Words Representation")
    inputs = [0]*len(words)
    for inputWord in cleanedInSen: ##for every user inputed word
        for index, bagWord in enumerate(words): ##for every word in bag word matrix
            if(bagWord == inputWord): ##if the word is in the words represented in NN input
                inputs[index] = 1
    return np.array(inputs)

import nltk
import numpy as np
import random
import pickle
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords, wordnet
import json
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

##This Module is made for building Keras Models
##Edit the intents.json accordingly and then run
##runTraining() in order to make model

lemmatizer = WordNetLemmatizer()
words=[]
classes = []
documents = []
ignore_words = ['?', '!', "'s", ',', '<', '>', "'", '"', 'a', 'the', 'and', 'be']

data_file = open('Resources/intents.json').read()
intents = json.loads(data_file)


def nltkTag2WordnetTag(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

for intent in intents['intents']:
    for pattern in intent['patterns']:

        # take each word and tokenize it
        w = []
        for word, tag in pos_tag(word_tokenize(pattern)):
            wntag = nltkTag2WordnetTag(tag)
            if not wntag:
                lemma = word.lower()
            else:
                lemma = lemmatizer.lemmatize(word.lower(), wntag)
            if(lemma not in ignore_words):
                w.append(lemma)
        words.extend(w)
        # adding documents
        documents.append((w, intent['tag']))
        # adding classes to our class list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = sorted(list(set(words)))
pickle.dump(words, open('Resources/words.pkl', 'wb'))
pickle.dump(classes, open('Resources/classes.pkl', 'wb'))


def runTraining():
    """Trains and Saves Keras Model"""
    trainingData = []
    ####creates bag of words
    for doc in documents:
        inputs = []
        doc_words = doc[0]
        for word in words:
            if word in doc_words:
                inputs.append(1)
            else:
                inputs.append(0)

        ###creates expected output
        correctOutput = list([0] * len(classes))
        correctOutput[classes.index(doc[1])] = 1

        trainingData.append([inputs, correctOutput])

    random.shuffle(trainingData)
    trainingData = np.array(trainingData)

    trainingInputs = list(trainingData[:,0])
    trainingExpectedOutputs = list(trainingData[:,1])
    makeModel(trainingInputs, trainingExpectedOutputs)

def makeModel(inputs, expectedOutputs):
    model = Sequential()
    model.add(Dense(100, input_shape=(len(inputs[0]),), activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(50, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(len(expectedOutputs[0]), activation='softmax'))

    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    hist = model.fit(np.array(inputs), np.array(expectedOutputs), epochs=200, batch_size=5, verbose=1)
    model.save('mymodel.h5', hist)


import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' ##stops TF from wining about CPU
import json
import pickle
import numpy as np
from keras.models import load_model

#NN and intents initizilation
intents = json.loads(open('Resources/intents.json').read())
list_of_intents = intents['intents']
model = load_model('Resources/mymodel.h5')
classes = pickle.load(open('Resources/classes.pkl', 'rb'))

def runNetwork(inputs):
    print("Running Keras Model")
    res = model.predict(np.array([inputs]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    greatestIndex = results[0][0]
    return classes[greatestIndex]
import json
import random
import os
from gtts import gTTS
# from faceManager import makeAFace, displaySmile

intents = json.loads(open('Resources/intents.json').read())
list_of_intents = intents['intents']

def respond(responseType):
    if responseType == "face":
        #makeAFace() #Only for RasPi
        print("*Makes a Face*")
    else:
        for i in list_of_intents:
            if (i['tag'] == responseType):
                result = random.choice(i['responses'])
        sayText(result)
    print("Finished")

def sayText(result):
    responseAudio = gTTS(result, lang='en')
    responseAudio.save('Resources/response.mp3')
    print("Response: ", result)

    ##Rasbian
    #os.system('omxplayer Resources/response.mp3')

    ##Windows
    #os.system(“start Resources/response.mp3”)

    #Mac
    os.system("afplay Resources/response.mp3")

    #displaySmile() ##Only for RasPi
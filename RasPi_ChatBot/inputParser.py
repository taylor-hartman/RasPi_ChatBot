import random
import json
from RasPi_ChatBot.NLP import cleanSentence, makeBag
from RasPi_ChatBot.networkRunner import runNetwork
from RasPi_ChatBot.responseGenerator import respond, sayText
intents = json.loads(open('Resources/intents.json').read())
list_of_intents = intents['intents']

def analyzeUserInputContent(text, textCase):
    print("Parsing Input")
    if textCase == 0:
        cleanedSen = cleanSentence(text)
        inputBagRep = makeBag(cleanedSen)
        responseClass = runNetwork(inputBagRep)
        respond(responseClass)
    elif textCase == 1: ##Indicates API was unreachable or unresponsive
        result = random.choice(list_of_intents[1]['responses']) ##chooses a response with 'broken' tag
        sayText(result)
    else: ##Indicates API did not recognize speech
        result = random.choice(list_of_intents[0]['responses']) ##chooses a response with 'confused' tag
        sayText(result)
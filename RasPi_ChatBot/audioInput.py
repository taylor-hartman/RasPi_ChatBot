import speech_recognition as sr
import time

def getAudioInput():
    """Collects Speech and converts to text using Google Speech API
    Returns:
    text - a string of the said speech
    textCase - an int that represents if the API was reachable and if it recognized the speech or not"""
    r = sr.Recognizer()
    r.pause_threshold = 0.6
    mic = sr.Microphone()
    with mic as source:
        time.sleep(1)
        print("Listening for input")
        inputSpeech = r.listen(source, phrase_time_limit=8)
    try:
        text = r.recognize_google(inputSpeech)
        textCase = 0
    except sr.RequestError: ##API was unreachable or unresponsive
        text = None
        textCase = 1
    except sr.UnknownValueError: ##API did not recognize speech
        text = None
        textCase = 2
    print("Input gathered")
    return text, textCase
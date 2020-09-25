print("Importing packages")
# import RPi.GPIO as GPIO ##Only for RasPi
import time
#from faceManager import wakeUp, listeningFace #Only for RasPi
from RasPi_ChatBot.audioInput import getAudioInput
from RasPi_ChatBot.inputParser import analyzeUserInputContent

#############Code For Desktop###################
if __name__ == "__main__":
        ##Collects Input
        input = getAudioInput()
        ##Sends Input to parser script which decides where to send it from there
        analyzeUserInputContent(input[0], input[1])
        time.sleep(0.05)
################################################

#############Code For Rasberry Pi###############
# #GPIO Initizilization
# GPIO.setwarnings(False) # Ignore unnecessary warning
# GPIO.setmode(GPIO.BCM) # Use the physical numbering
# GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Sets pin 18 as input pin and initial value to off
#
# if __name__ == "__main__":
#     wakeUp()  ## plays wake up animation on boot
#     while True: ##Checks if button was pressed every 0.05 seconds
#         if GPIO.input(18):
#             if not gettingAudio:
#                 gettingAudio = True
#                 listeningFace()
#                 input = getAudioInput()
#                 analyzeUserInputContent(input[0], input[1])
#         time.sleep(0.05)
##################################################
import aiml
import os
import time, sys
#from gtts import gTTS
#from pygame import mixer
import pyttsx3
import warnings
import threading
from os import system
from PyQt4.QtCore import QSize
from PyQt4.QtGui import QApplication, QLabel, QMovie, QPainter, QFontMetrics 


mode = "text"
if len(sys.argv) > 1:
    if sys.argv[1] == "--voice" or sys.argv[1] == "voice":
        try:
            import speech_recognition as sr
            mode = "voice"
        except ImportError:
            print("\nInstall SpeechRecognition to use this feature.\nStarting text mode\n")

terminate = ['bye','buy','shutdown','exit','quit','gotosleep','goodbye']

class QTextMovieLabel(QLabel):
    def __init__(self, fileName):
        QLabel.__init__(self)
       
        m = QMovie(fileName)
        m.start()
        self.setMovie(m)

    def setMovie(self, movie):
        QLabel.setMovie(self, movie)
        s=movie.currentImage().size()
        self._movieWidth = s.width()
        self._movieHeight = s.height()

 
def main():
    import sys
    app = QApplication(sys.argv)
    l = QTextMovieLabel('jelvis.gif')
    l.setWindowTitle("JELVIS")
    l.show()
    app.exec_()


def offline_speak(jarvis_speech):
    engine = pyttsx3.init()
    engine.say(jarvis_speech)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Talk to JELVIS: ")
        audio = r.listen(source)
    try:
        print r.recognize_google(audio)
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        #offline_speak("I couldn't understand what you said! Would you like to repeat?")
        return(listen())
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    #kernel.saveBrain("bot_brain.brn")

# kernel now ready for use

def orgin():
    while True:
        if mode == "voice":
            response = listen()
        else:
            response = raw_input("Talk to JELVIS : ")
        if response.lower().replace(" ","") in terminate:
            break
        jarvis_speech = kernel.respond(response)
        print "JELVIS: " + jarvis_speech
        offline_speak(jarvis_speech)



t = threading.Thread(name='orgin', target=orgin)
w = threading.Thread(name='main', target=main)

w.start()
t.start()
    





 

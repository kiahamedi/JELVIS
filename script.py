import aiml
import os
import time, sys
import pyttsx3
import warnings
import threading
import pocketsphinx
from os import system
from PyQt4 import QtGui
import speech_recognition as sr
from PyQt4.QtCore import QSize
from PyQt4.QtGui import QApplication, QLabel, QMovie, QPainter, QFontMetrics 
import urllib3


mode = "voice"
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

def internet_on():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False

def offline_speak(jarvis_speech):
    engine = pyttsx3.init()
    engine.say(jarvis_speech)
    engine.runAndWait()

def listen():
    #try:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Talk to JELVIS: ")
        audio = r.listen(source)
    try:
        #print (r.recognize_google(audio))
        #return  r.recognize_google(audio)
        if internet_on() == True:
            print (r.recognize_google(audio))
            return  r.recognize_google(audio)
        else:
            print (r.recognize_sphinx(audio))
            return  r.recognize_sphinx(audio)

    except sr.UnknownValueError:
        #offline_speak("I couldn't understand what you said! Would you like to repeat?")
        return(listen())
    except sr.RequestError as e:
        print("Could not request results from sphinx service; {0}".format(e))
    #except sr.UnknownValueError:
    #    return(listen())


kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    #kernel.saveBrain("bot_brain.brn")

# kernel now ready for use
def orgin():
    try:
        while True:
            if mode == "voice":
                response = listen()
            else:
                response = raw_input("Talk to JELVIS : ")
            if response.lower().replace(" ","") in terminate:
                #break
                response = listen()    
            jarvis_speech = kernel.respond(response)
            print ("JELVIS: " + jarvis_speech)
            offline_speak(jarvis_speech)
    except:
       return(orgin())


t = threading.Thread(name='orgin', target=orgin)
w = threading.Thread(name='main', target=main)

w.start()
t.start()



 

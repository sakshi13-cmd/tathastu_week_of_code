import webbrowser as wb
import speech_recognition as sr
from tkinter import import *
from time import ctime
import time
import os
from gtts import gTTs
import pygame
from pygame import mixer
from aifc import data
def speak(audioString):
    global x
    b= audioString
    if len(b)==0:
        return 
    tts =gTTs(text=b, lang='en-us')
    tts.save("voice%s.mp3" %(x))
    pygame.init()
    pygame.display.set_mode((2,1))
    mixer.music.load("voice%s.mp3" %(x))
    mixer.music.play(0)
    
    x+=1
    clock=pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
    
    
    
def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak..")
        audio = r.listen(source)
        print("heard...")
    data =" "
    try:
        data = r.recognize_google(audio)
        print("you said :" +data)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("could not request results from Google Speech Recognition service;{0}".format(e))
            return data

def jarvis(data):
    if "how r you " in data:
        speak("i m fine")
    elif "what time is it" in data:
        speak(ctime())
    elif "where is " in data:
        data = data.split(" ")
        location =data[2]
        speak("hold on sam i will show you where " +lacation+"is")
        wb.open_new_tab("https://www.google.ni/maps/place/" +location + "/&amp;")
    else:
        speak("i didn't undestand")
time.sleep(0.5)
x=0
print("starting program")
speak("Hi!sam ,what can i do for you?")
data = recordAudio()
jarvis(data)
speak("turning off the program")
print("run complete")

        
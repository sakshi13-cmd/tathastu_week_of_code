import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("say something!")
    audio = r.listen(source)
try:
    print("Google Speech Recognition things you said" + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could understand audio")
except sr.RequestError as e:
    print("could not request results from Google Speech Recognition service;{0}".format(e))
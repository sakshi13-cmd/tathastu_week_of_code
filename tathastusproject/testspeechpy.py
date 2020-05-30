import speech_recognition as sr
from pip._vendor.chardet.langcyrillicmodel import IBM855_char_to_order_map
r= sr.Recognizer()
with sr.Microphone() as source:
    print("say something")
    audio = r.listen(source)
    print("heard")
try:
    print("Sphinx thinks you said "+ r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")

except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
try:
    print("Google Speech Recognition thinks you said " +r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("could not request results from Google Speech Recognition service;{0}".format(e))
WIT_AI_KEY ="INSERT WIT_AI API KEY HERE "
try:
    print("Wit.ai thinks you said "+ r.recognize_sphinx(audio , key=WIT_AI_KEY ))
except sr.UnknownValueError:
    print("Wit.ai  could not understand audio")
except sr.RequestError as e:
    print("could not request results from Wit.ai service;{0}".format(e))
BING_KEY ="INSERT BING  API KEY HERE"
try:
    print("Microsoft Bing Voice Recognition thinks you said "+  r.recognize_bing(audio , key=BING_KEY ))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition  could not understand audio")
except sr.RequestError as e:
    print("could not request results from Microsoft Bing Voice Recognition  service;{0}".format(e))
AZURE_SPEECH_KEY ="INSERT AZURE SPEECH API KEY HERE"
try:
    print("Microsoft Azure thinks you said "+ r.recognize_azure(audio , key=AZURE_SPEECH_KEY))
except sr.UnknownValueError:
    print("Microsoft Azure Speech could not understand audio")
except sr.RequestError as e:
    print("could not request results from Wit.ai service;{0}".format(e))
HOUNDIFY_CLIENT_ID = "INSERT HOUNDIFY CLIENT ID  HERE"
HOUNDIFY_CLIENT_KEY = "INSERT HOUNDIFY CLIENT KEY  HERE"
try:
    print("Houndify thinks you said "+  r.recognize_houndify(audio ,client_id= HOUNDIFY_CLIENT_ID , client_key= HOUNDIFY_CLIENT_key))
except sr.UnknownValueError:
    print("Houndify  could not understand audio")
except sr.RequestError as e:
    print("could not request results from Houndify service;{0}".format(e))
IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE"
IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE"
try:
    print("IBM Speech to Text thinks you said "+ r.recognize_ibm(audio , username=IBM_USERNAME,password=IBM_PASSWORD))
except sr.UnknownValueError:
    print("IBM Speech to Text  could not understand audio")
except sr.RequestError as e:
    print("could not request results from IBM Speech to Text service{0}".format(e))
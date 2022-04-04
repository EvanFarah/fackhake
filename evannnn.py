import urllib.request
import random
import keyboard
import pyryhme
import speech_recognition  as sr
import playsound
def get_voice():
     filename = urllib.request.urlopen("https://ia802609.us.archive.org/3/items/beatboxset1/battleclip_daq.ogg")
     return filename
v = playsound.playsound(filename)

r = sr.Recognizer
source = sr.Microphone
get_audio = r.listen(source)
def get_rap(object):
    while True:
               h = ("hi")
               return h
nouns = ("puppy", "car", "rabbit", "girl", "monkey")  
verbs = ("runs", "hits", "jumps", "drives", "barfs")
adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")
hi = r.recognize_google(get_audio)
adj = pyrhyme.RyhmeBrain(hi)
num = random.randrange(0,5)
get_voice.v(nouns[num] + ' ' + verbs[num] + ' ' + adv[num] + ' ' + adj[num])
h = input("")
if h == ("no"):
    while True:
               break

if h == ("yes"):
    while True:
               continue

try:
    get_rap(object)
    print("program has started.")
except KeyboardInterrupt:
    exit(1)
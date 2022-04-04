import pyttsx3
import random
import keyboard
import subprocess
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
nouns = ("puppy", "car", "rabbit", "girl", "monkey")  
verbs = ("runs", "hits", "jumps", "drives", "barfs")
adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")
engine = pyttsx3.init()
engine.say("please, say the last word in, your sentence.")
engine.runAndWait()
hi = r.recognize_google(get_audio)
engine.say("would you like to disable your michrophone for now?")
by = r.recognize_google(get_audio)
if by == ("yes"):
        p = subprocess.Popen(['C:\Windows\System32\mblctr.exe'])       
        keyboard.press_and_release('m')
        p.kill()
if hi == (""):
        engine.say("would you like to test your microphone? we got no feedback from, your microphone.")
        engine.say("for yes, type y on your, computer. for no, type n on your computer.")
        ty = input("")
if ty == ("y"):
    engine.say("please, say something.")  
if sr.UnknownValueError:
             engine.say("your michrophone does not work or, is not setup properly.")
if sr.UnknownValueError == False:
         engine.say("your microphone does, work.")
if ty == ("Y"):
    engine.say("please, say something.")  
if sr.UnknownValueError:
             engine.say("your michrophone does not work or, is not setup properly.")
if sr.UnknownValueError == False:
         engine.say("your microphone does, work.")

adj = pyrhyme.RyhmeBrain(hi)
num = random.randrange(0,5)
get_voice.v(nouns[num] + ' ' + verbs[num] + ' ' + adv[num] + ' ' + adj[num])
h = input("do you want to end this program? y for yes n for no.")
if h == ("y"):
    while True:
               continue
    print("program will, continue")
if h == ("Y"):
    while True:
               continue
    print("program will, continue")

if h == ("n"):
    while True:
               break
    print("program has, stoped.")
if h == ("N"):
    while True:
               break
    print("program has, stoped.")
try:
    get_rap(object)
except KeyboardInterrupt:
   exit(1)
if __name__ == "__main__":
     print("program has, started.")

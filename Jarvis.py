from datetime import datetime
from email.mime import audio
import speech_recognition as sr
import pyttsx3
import datetime # for date time which is used in line 12

engine=pyttsx3.init('sapi5') #for collecting voice
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id) # for changing male voice, if i write voice[1].ide, then it's create female voice.
def speak(audio): #for jervis speaking
    engine.say(audio)# engine say this audio
    engine.runAndWait()

def wishMe(): # for wish me
    hour=int(datetime.datetime.now().hour) # we define hour form import datehour library which is say date hour
    if hour>=0 and hour< 12: # for morning 12am to noon 12pm
        speak("Good morning")
    elif hour>=12 and hour<18:# for noon to evening 6 pm
        speak("Good afternoon")
    elif hour>18 and hour<22: # for 6pm to 10pm
        speak("Good evening")
    else: #for 10pm to night 12am
        speak("Good night")

    speak(" hi i am jervis. my crator is Mr. soham") # for speaking jervis himself
    #pass

def takecommand(): # for take spech from user and give us string as output
    r=sr.Recognizer
    with sr.Microphone() as source: # for take input from user by microphone
        print("Listening......")
        r.pause_threshold=1 # when user speak sometging then jervis wait 1 sec
        audio=r.listen(source)
    try: #whe error did
        print("recognisting.....")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said: {query}\n ")
    except Exception as e:# when jervis did'nt understand what user said
        #print(e)
        print("say that again.....")
        return "None"
    return query

if __name__=="__main__":
    #speak("soham is a good boy") # jarvis say this sentence
    wishMe()# for call wishme function in this way jervis wishme thats way i define in this program
    takecommand()
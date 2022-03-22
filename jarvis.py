import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To convert voice into text
def takecommad():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}") 


    except Exception as e:
        speak("say that again please.....")
        return "none"
    return query   

#to wish 
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morining")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis sir . please tell me how can i help you")            

             



if __name__=="__main__":
    wish()
    #while True:
    if 1:

        query = takecommad().lower()

        #logic building for tasks

        if "open notepad" in query:
            npath = "C:\\windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif"open command prompt" in query:
            os.system("start cmd") 


        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("according to wikipedia")
            speak(results)
            print(results)


        elif "open youtube " in query:
            webbrowser.open("https://www.youtube.com/")





    
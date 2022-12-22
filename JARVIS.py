import pywhatkit as wt
import cv2
from ast import Break
import random
import smtplib
from http import server
import os
import smtplib
import wikipedia
import webbrowser
from unittest import result
import pyttsx3
import datetime
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)





def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    #speak("I am jarvis sir. please tell me how may i help you")
    speak("I am shivani sir. please tell me how may i help you")
    
def takeCommand():
    #it takes microphone input from user and retuerns sring outpuet
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        print("Listening.....")
        #r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again pleae")
        return"None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vsh4420@gmail.com', 'akdpdenzxatycpbq')
    server.sendmail('vsh4420@gmail.com', to, content)
    server.close()
if __name__ == "__main__":
    wishMe()
    if 1:
        query = takeCommand().lower()
        speak('start')
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print("running")
            print(results)
            speak(results)
            
        elif 'play music' in query:
            music_dir = 'C:\\Users\\91831\\Desktop\\vikas'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
        
            os.startfile(os.path.join(music_dir, songs[0]))
            speak ("start")
        elif 'open notepad' in query:
            npath = 'C:\\Windows\\system32\\notepad.exe'
            os.startfile(npath)
            speak("opening notpad")
        

        #elif 'open youtube' in query:
           # webbrowser.open("youtube.com")
            #speak("start")
        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.inshow('webcam',img)
                k = cv2.wailkey(50)
                if k==27:
                    Break
                cap.release()
                cv2.destroyAll()
                speak("end")
        elif "open command" in query:
            os.system("start cmd")
            speak("open google")
        elif 'open google' in query:
            speak('sir, what should i search on google')
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'email to vikas' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vikashsahu4420gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend vikas bhai. I am not able to send this email")    

        

            
        
import pyttsx3 #pip install pyttsx3
import datetime
import webbrowser
import os

#Jarvis
engine = pyttsx3.init('sapi5')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<15:
        speak("Good Afternoon!")
    elif hour>=15 and hour<=20:
        speak("Good Evening!")
    else:
        speak("Good Night!")  
    speak("I am Jarvis Sir. Please tell me how may I help you")
    askMe()

def askMe():
    query = input("Enter command : ")
    
    if 'wikipedia' in query:
            webbrowser.open("https://wikipedia.com/")
            askMe()

    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com/")
        askMe()

    elif 'open google' in query:
        webbrowser.open("https://google.com")
        askMe()

    elif 'open stackoverflow' in query:
        webbrowser.open("https://stackoverflow.com")
        askMe()

    elif 'play music' in query:
        music_dir = 'E:\\Tracks'
        songs = os.listdir(music_dir)
        print(songs)    
        os.startfile(os.path.join(music_dir, songs[0]))
        askMe()

    elif 'the time' in query:
        nowTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(datetime.datetime.now())
        speak("Sir, the time is "+ nowTime)
        askMe()

    elif 'open code' in query:
        codePath = "E:\\Programming Life"
        os.startfile(codePath)
        askMe()
        
wishMe()


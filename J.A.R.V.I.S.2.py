import getpass
from random import randint
import json
import requests
import pyautogui
import time
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
import smtplib

#plz enter your chrome_path and don't forgot to write %s in the chrome_path end
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#i am using microsoft david for my jarvis you can also make friday with the help of ([1].id)
engine.setProperty("voice", voices[0].id)
password = "hello"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

    speak("I am jarvis your assistant how may i help you")

def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\\scr\\screenshot.png") #path where screenshot will be saved

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
        
def passWord():
    n = getpass.getpass('>> ')

    if n == password:
        print("The password is ended with status (DONE)\n")

    else:
        print("The code is exited with status (NOT DONE)\nSorry you can't able to use jarvis")
        time.sleep(5)
        quit()

if __name__ == "__main__":
    passWord()
    wishMe()
    while True:
        query = takeCommand().lower()
        print(query) 

        if "how are you" in query:
            speak("I am fine and pray for your well being")
            print("I am fine and pray for your well being")
        elif "news" in query:
            i
            url="your newsapi key"
            page=requests.get(url)
            text=page.text
            news=json.loads(text)
            articles=news["articles"]
            newsPoint=articles[randint(0,len(articles)-1)]['title']
            print(newsPoint)
            speak(newsPoint)
        elif "who are you" in query:
            speak("I am your assistant jarvis")
            print("I am your assistant jarvis")
        elif "take screenshot" in query:
            speak("taking screenshot")
            screenshot()
        elif "open wikipedia" in query:
            speak("here it is")
            webbrowser.get(chrome_path).open("wikipedia.com")
        elif "open my yt channel" in query:
            speak("here it is")
            webbrowser.get(chrome_path).open("https://www.youtube.com/channel/UC556qZbJolO8iLxh1n2u4vQ?view_as=subscriber")
        elif "open twitter" in query:
            speak("here it is")
            webbrowser.get(chrome_path).open("twitter.com")
        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)
        elif "open youtube" in query:
            speak("here it is")
            webbrowser.get(chrome_path).open("youtube.com")
        elif "play music" in query:
            speak("ok sir,here it is")
            music_dir = "E:\\music2"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "play song" in query:
            speak("ok sir,here it is")
            # plz write your place where the song you have placed 
            music_dir = "E:\\music2"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
            print(strTime)
        elif "todays weather" in query:
            speak("ok sir, here it is")
            webbrowser.get(chrome_path).open("https://weather.com/en-IN/weather/today/l/c1147cf4cecd551f01f6bcfaa0393f60bb53387712d166cda2f6e2efa58328da")
        elif "thanks" in query:
            speak("my pleasure")
            print("my pleasure")
        elif "thanks jarvis" in query:
            speak("welcome sir")
            print("welcome sir")
        elif "google search" in query:
            speak("recognizing")
            speak("sir, plz enter what do you want to search")
            pc = input("Enter google search = ")
            speak("searching google...")
            webbrowser.get(chrome_path).open("https://google.com/?q="+pc)
        elif "abort" in query:
            speak("closing program thanks sir for giving me your precious time")
            quit()
        else:
            print("sorry the command you entered is not satisfied")
            speak("sorry the command you entered is not satisfied")
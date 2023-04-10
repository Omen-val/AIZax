import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import webbrowser
from requests import get
import wikipedia
import pywhatkit as pywt
import sys
import pyjokes
import requests
import instaloader
import time
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


# -------FUNCTIONS----------- #

# Speak Function Below
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# To Convert Voice to Text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=2,phrase_time_limit=5)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User Said: {query}")

    except Exception as e:
        speak("Say that again please....")
        return "none"
    
    return query



# Wish Function
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <=12:
        speak("Good Morning!")

    elif hour>12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I'm Zax, Please tell me how may I help you?")

def multiply():
    try:
        speak("PLease Enter the first Number")
        a = int(input("Please Enter first the number: "))
        speak("PLease Enter the second Number")
        b = int(input("Please Enter the second number: "))
        product = a * b
        speak(f"The answer is {product}")

    except Exception as e:
        speak("Please Enter a number!")

def add():
    try:
        speak("PLease Enter the first Number")
        a = int(input("Please Enter the first number: "))
        speak("PLease Enter the second Number")
        b = int(input("Please Enter the second number: "))
        sum = a + b
        speak(f"The answer is {sum}")

    except Exception as e:
        speak("Please Enter a number!")



def minus():
    try:
        speak("Please Enter first number")
        a = int(input("Please Enter the first number: "))
        speak("Please Enter second number")
        b = int(input("Please Enter the second number: "))
        diff = a - b
        speak(f"The answer is {diff}")

    except Exception as e:
        speak("Please Enter a number!")


def devide():
    try:
        speak("Please Enter first number")
        a = int(input("Enter the first number: "))
        speak("Please Enter second number")
        b = int(input("Please Enter the second number: "))
        que = a / b
        speak(f"The division answer is {que}")

    except Exception as e:
        speak("Please Enter a number!")



if __name__ =="__main__":
    wish()

    while True:
        query = takecommand().lower()

        # Task Execution



        if 'open notepad' in query:
            path = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(path)

        elif 'multiply' in query:
                speak("Ok, Sir!")
                time.sleep(1)
                multiply()

        elif 'addition' in query:
            speak("Ok, Sir!")
            time.sleep(1)
            add()

        elif 'divide' in query or 'division' in query:
            speak("Ok, Sir!")
            time.sleep(1)
            devide()

        elif 'minus' in query:
            speak("Ok, Sir!")
            time.sleep(1)
            minus()

        elif 'close notepad' in query:
            speak("Closing Notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'quit' in query:
            speak("Okay, call me anytime!")
            break

        elif 'open word' in query:
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word 2016.lnk"
            os.startfile(path)

        elif 'close word' in query:
            speak("Closing Word...")
            os.system("taskkill /f /im Word 2016.lnk")

        elif 'open command' in query:
            os.system("start cmd")

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:

                ret, img = cap.read()
                cv2.imshow('Zax Cam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break

            cap.release()
            cv2.destroyAllWindows()

        elif 'open viber' in query:
            path = "C:\\Users\\IT BD\\AppData\\Local\\Viber\\Viber.exe"
            os.startfile(path)

        elif 'close viber' in query:
            speak("Closing Viber...")
            os.system("taskkill /f /im Viber.exe")

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP Address is {ip}")

        elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir the time is {strTime}")

        elif 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            query = query.replace("zax", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'google' in query:
            speak("What Should I search on google?")
            search = takecommand().lower()

            webbrowser.open(f"{search}")

        elif 'youtube search' in query:
            speak("This is what I found")
            query = query.replace("youtube search", "")
            query = query.replace("zax")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            pywt.playonyt(query)
            speak("Done!")

# ------------SEND WHATSAPP MESSAGE----------------#

        # elif 'send message' in query:
        #     speak("What should I message?")
        #     msg = takecommand().lower()
        #     pywt.sendwhatmsg("+8801676604750", msg, 1,21)

#--------------------------------------------------#


        elif 'play a song' in query:
            speak("What is the name of the song?")
            song = takecommand().lower()
            pywt.playonyt(song)

        elif 'no thanks' in query:
            speak("Ok, Bye!")
            sys.exit()


        elif 'you need a break' in query:
            speak("Ok, See you!")
            sys.exit()

        elif 'shutdown computer' in query:
            os.system("shutdown /s /t 5")

        elif 'restart computer' in query:
            os.system("shutdown /r /t 5")

        elif 'where are we' in query or 'where am i' in query or 'location' in query:
            speak("Wait Sir, Let me check..")
            try:
                ipAdrs = requests.get('https://api.ipify.org').text
                print(ipAdrs)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdrs+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"Sir, I'm not sure but, we are in the {city} of country {country}")

            except Exception as e:
                speak("Sir, I was unble find our loction due to network issues.")
                pass

        
        elif 'instagram profile' in query or 'insta pfp' in query:
            speak("Please enter the Instagram Profile name correctly!")
            name = input("Enter the Username:- ")
            webbrowser.open(f'https://instagram.com/{name}')
            speak(f"Sir, here is the instagram profile of {name}")
            time.sleep(5)
            speak("Would you like to download the profile picture of this user")
            answer = takecommand().lower()
            if 'yes' in answer or 'yeah' in answer:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("Sir, Profile Pic has been downloaded in our main folder")

            else:
                pass


        elif 'take a screenshot' in query or 'take screenshot' in query:
            speak("Please enter the name of the screenshot file.")
            screenstnm = input("Enter the Name: ")
            speak("Sir please hold still, I'm taking a screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{screenstnm}.png")
            speak("I'm done sir!")
            time.sleep(1.4)

        
        elif 'hide my files' in query or 'hide all files' in query or 'make it visible' in query:
            speak("Sir, Should I hide the files or make it visible")
            condition = takecommand().lower()

            if 'hide' in condition:
                os.system("attrib +h /s /d")
                speak("Sir, All files are now hidden")

            elif 'visible' in condition:
                os.system("attrib -h /s /d")
                speak("Sir, All files are now visible")

            elif 'leave it' in condition or 'leave for now' in condition:
                speak("Ok, Sir!")

            
            


# ---------CONVERSATION---------- #

        elif 'hello' in query:
            speak("Hi!, How are you?")

        elif 'i am fine' in query:
            speak("That's Nice")

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'who are you' in query:
            speak("I'm your personal AI Assistant. My name is Zax")

        elif 'zax' in query:
            speak("Yes Sir?")

# ------CONVERSATION END--------- #

        speak("Do you have any other work?")


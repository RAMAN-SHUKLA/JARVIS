import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import os
import time
import subprocess
import wikipedia
import pywhatkit as pwk
import user_config
import smtplib,ssl
import openai
import mtranslate

# Initialize Text-to-Speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command(): 
    # Initialize recognizer
    content = ""
    while content == "":
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            content = r.recognize_google(audio, language='en-in')
            
            content=mtranslate.translate(content,to_language="en-in")
            print("You said: " + content)
        except Exception:
            print("Please try again...")
            return ""
    
    return content

def main_process():
    while True: 
        request = command().lower()
        if "hello" in request:
            speak("Welcome , How can I help you")
        elif "play music" in request:
            speak("Playing Music")
            songs = [
                "https://youtu.be/pqZuSz8_2DM?si=MFSPmfsHb8VVBoPn",
                "https://youtu.be/QxddU3sjVRY?si=M67KLSujcbYrVak0",
                "https://youtu.be/A66TYFdz8YA?si=AWaT_BRs1ggq6o13",
                "https://youtu.be/HVY2VejF_YM?si=BNrgrMdfkNE3US5c",
                "https://youtu.be/OIv0FLrbnGE?si=hzQ1krFEelckzgCo"
            ]
            webbrowser.open(random.choice(songs))
        elif "what is time now" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            speak("It is " + now_time + " now")
        elif "who are you" in request:
            speak("Hello! I’m JARVIS a personal AI assistant created by my master Raman Shukla, here to help, organize, and simplify your tasks. From answering questions to managing reminders, playing music, and even sending messages I’ve got you covered. Just say the word, and I’m ready to assist! ")

        elif "what is date today" in request:
            now_date = datetime.datetime.now().strftime("%d:%m:%Y")
            speak("Date is " + now_date + " today")  
        elif "new task" in request:
            task = request.replace("new task", "").strip()
            if task:
                speak("Adding task: " + task)
                with open("task.txt", "a") as file:
                    file.write(task + "\n")
        elif "speak the task" in request:
            if os.path.exists("task.txt") and os.path.getsize("task.txt") > 0:
                with open("task.txt", "r") as file:
                    tasks = file.read()
                speak("Work we have to do is " + tasks)
                os.remove("task.txt")
                speak("Tasks have been deleted after reading.")
            else:
                speak("There are no tasks to read.")
        elif "show work" in request:
            if os.path.exists("task.txt") and os.path.getsize("task.txt") > 0:
                with open("task.txt", "r") as file:        
                    tasks = file.read()
                notification.notify(
                    title="Work of Today",
                    message=tasks
                )
                os.remove("task.txt")
                speak("Tasks have been deleted after showing.")
            else:
                speak("There are no tasks to show.")

        elif "open youtube" in request:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        elif "open spotify" in request:
            speak("Opening Spotify")
            webbrowser.open("https://www.spotify.com")
        elif "open facebook" in request:
            speak("Opening Facebook")
            webbrowser.open("https://www.facebook.com")
        elif "open instagram" in request:
            speak("Opening Instagram")
            webbrowser.open("https://www.instagram.com")

        elif "open" in request:
            query = request.replace("open", "").strip()
            pyautogui.press("super")
            pyautogui.typewrite(query)
            time.sleep(2)
            pyautogui.press("enter")
        elif "screenshot" in request:
            screenshot = pyautogui.screenshot()
            file_path = "screenshot.png"
            screenshot.save(file_path)
            speak("Screenshot taken and opening now.")
            subprocess.Popen([file_path], shell=True)
            time.sleep(5)
            os.remove(file_path)
            speak("Screenshot deleted after viewing.")
        elif "wikipedia" in request:
            query = request.replace("wikipedia", "").strip()
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif "search google" in request:
            query = request.replace("search google", "").strip()
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak("Searching Google for" + query)
        elif "send whatsapp" in request:
            pwk.sendwhatmsg("+91 955055XXXX","hello",21,50,30)
        elif "send email" in request:
            s=smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            
            s.login("youremail@gmail.com",user_config.gmailpassword)
            message=""" 
            hello 
            how can i help you?
            thank you
            """
            s.sendmail("youremail@gmail.com","targatedemail@gmail.com",message)
            s.quit()    
            speak("Email Sent Successfully")
        
        elif"ask to chat " in request:
            request=request.replace("jarvis","")
            request=request.replace("ask to chat","")

            print(request)
            speak("you have reached to your daily limit of Using Chatgpt 4 O")


main_process()


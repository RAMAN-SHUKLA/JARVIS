import pyttsx3

engine=pyttsx3.init()
voices=engine.getProperty('voices')
for i in voices:
    print(i)
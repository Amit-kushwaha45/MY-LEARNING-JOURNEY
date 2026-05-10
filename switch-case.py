import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pywhatkit
import os
import wikipedia

# Voice engine start

print("press1= intro")
print("press2= shutdown pc")
print("press3= open file manager")
print("press4= open youtube")
print("press5= opening github")
print("press6= play song")
print("press7= search by there name")
print("press8= open google")
print("press9= open linkdin")
print("press10= check time")
press=int(input("enter your number"))

if(press==10):
        time = datetime.datetime.now().strftime("%H:%M")
        print("Current time is " + time)
elif(press==1):
    print("hello amit")

elif(press==2):
    print("shutting down")
    os.system("shutdown /s /t 1")

elif(press==3):
    print("opening File Manager")
    os.system("File Manager")

elif(press==4):
    print("opening youtube")
    webbrowser.open(f"https://www.youtube.com/")

elif(press==5):
    print("opening github")
    webbrowser.open(f"https://github.com/Amit-kushwaha45")

elif(press==6):
    print("play song")
    pywhatkit.playonyt

elif (press==7):
        person=input("who is")
        info = wikipedia.summary(person, 2)
        print(info)
elif(press==8):
  print("opening google")
  webbrowser.open(f"https://google.com")

elif(press==9):
  print("opening linkdin")
  webbrowser.open(f"https://www.linkedin.com/in/amit-kushwaha-078127398/")

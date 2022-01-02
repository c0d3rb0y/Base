#1 for debug speech, 0 for none
debug = 0

if(debug == 1):
    print("BaseUtils v1.0.0 starting...")

import os
import threading

try:
    import pydub
except:
    print("pydub not found! attempting install...")
    os.system('cmd /c "pip install pydub"')
    import pydub

try:
    import speech_recognition as sr
except:
    print("speech_recognition not found! attempting install...")
    os.system('cmd /c "pip install SpeechRecognition"')
    import speech_recognition as sr

try:
    import pyaudio
except:
    print("pyaudio not found! attempting install...")
    os.system('cmd /c "pip install pipwin"')
    os.system('cmd /c "pipwin install pyaudio"')
    import pyaudio

try:
    import pyttsx3
except:
    print("pyttsx3 not found! attempting install...")
    os.system('cmd /c "pip install pyttsx3"')
    import pyttsx3


r = sr.Recognizer()

engine = pyttsx3.init()
engine.setProperty('rate', 150) 
voices = engine.getProperty('voices')   
engine.setProperty('voice', voices[1].id)
if(debug == 1):
    engine.say("Speech engine started.")
    engine.runAndWait()

def speak(phrase):
    engine.say(str(phrase))
    engine.runAndWait()

def voice(vc):
    engine.setProperty('voice', voices[vc].id)

#LISTEN IS BROKEN! I don't know why, but it is. Do not use this unless this message is not in the code anymore!
def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=2)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data, language="en-US", show_all=True)
        print(text)
        return text

def mods():
    try:
        import tkinter
    except:
        print("tkinter not found! attempting install...")
        os.system('cmd /c "pip install tkinter"')
        import tkinter
    m = tkinter.Tk()
    m.title("Mods")
    filelist = os.listdir(os.path.dirname(os.path.abspath(__file__)) + """\comp_mods""")
    filelist.remove("__init__.py")
    filelist.remove("__pycache__")
    Lb = tkinter.Listbox(m)
    i = 0
    for x in filelist:
        i += 1
        exec("Lb.insert(" + str(i) + ",\"" + x + "\")")
    Lb.pack()
    button = tkinter.Button(m, text='Close', width=25, command=m.destroy)
    button.pack()
    m.mainloop()

def command(cmdin):
    if(cmdin == "help"):
        return """All Vanilla Commands: help. opens this menu. math. a preinstalled module for simple operations. mods. opens module menu. quit. closes the software."""
    if(cmdin == "mods"):
        speak("Opening mod menu.")
        mods()
        return ""
    if(debug == 0):
        try:
            exec("from base.comp_mods import " + cmdin)
        except:
            i = 1
            filelist = os.listdir(os.path.dirname(os.path.abspath(__file__)) + """\comp_mods""")
            filelist.remove("__init__.py")
            filelist.remove("__pycache__")
            namelist = []
            for x in filelist:
                replaceX = x.replace(".py", "")
                namelist.append(replaceX)
            if cmdin in namelist:
                print("The current command crashed.")
            else:
                print("Command not found.")

                
            
    else:
        exec("from base.comp_mods import " + cmdin)
    return ""

if(debug == 1):
    speak("Speak shortcut defined.")

# DO ANYTHING AFTER THIS NEEDED


if(debug == 1):
    speak("BaseUtils started.")
#print("BaseUtils initiated.")

if __name__ == "__main__":
    mods()
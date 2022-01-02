from base.utils import *

try:
    mem = open("mem.txt", "a+")
except:
    mem = open("mem.txt", "x")
    mem.close()
    mem = open("mem.txt", "a+")

mem.seek(0)
if(mem.readline() != ""):
    print("Loaded voice config!")
else:
    #speak("hi, do you like this voice")
    speak("Hello! Welcome to Base, an AI platform that's made to be easy to customize. First off, should I keep this voice,")
    voice(0)
    speak("or do you like this one?")
    voice(1)

    #Screw this i'm making it keyboard based
    #Voice recognition can be a module later
    foundKW = 0
    """
    while foundKW == 0:
        speak("First, or second?")
        answer = dict(listen())
        try:
            list_of_all_values = [value for elem in answer[1]
                        for value in elem.values()]
        except:
            list_of_all_values = []
        print(list_of_all_values)
        if("second" in list_of_all_values):
            voice(0)
            print("SCND")
            foundKW = 1
            interactivity = "Thanks, didn't know if you'd choose me or not."
        if("first" in list_of_all_values):
            voice(1)
            print("FRST")
            foundKW = 1
            interactivity = "Nice, and thanks for choosing me over the other one."
        if(foundKW == 0):
            print("NONE")
            print("REAT")
            speak("I'm sorry, I didn't understand what you said. Please try again.")
            answer = listen()
    """
    while foundKW == 0:
        speak("Type 1 for first voice, and type 2 for second voice.")
        vt = input("Type 1 for first voice, and type 2 for second voice.\n")
        if(vt == "1"):
            voice(1)
            mem.write("1")
            interactivity = "Nice, and thanks for choosing me over the other one. Let's continue the tour."
            foundKW = 1
        if(vt == "2"):
            voice(0)
            mem.write("2")
            interactivity = "Thanks, didn't know if you'd choose me or not. Other one stole the show in the beginning, but it's ok. Anyways, moving on."
            foundKW = 1
        if(foundKW == 0):
            speak("Please try again, I did not recognize that as a number.")
    speak(interactivity)
    speak("You'll probably figure it out after looking around for a while, and typing aimlessly, but there is a simple help menu accessible by typing help. Try it!")
    if(input("Input Command: ").lower() == "help"):
        speak("Nice job! That was just a demo, but you probably get how this works by now.")
        
    else:
        speak("Good try, but that isn't how you say help. Basically, how almost everything here works is pretty simple.")
    speak("Type thing in, you get answer.")
    speak("Anyway, that wraps up my tour. Entering command mode.")

mem.seek(0)
aiType = mem.readline()

if(aiType == "1"):
    voice(1)
if(aiType == "2"):
    voice(0)

eggsit = 0
while eggsit == 0:
    cmdin = input("Input Command: ").lower()
    if (cmdin == "quit"):
        quit()
    else:
        speak(command(cmdin))
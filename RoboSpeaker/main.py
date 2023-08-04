import pyttsx3

if __name__ == "__main__":
    print("Welcome to RoboSpeaker Created by Mujaheed")
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125)
    while True:
        x = input("What do you want me to speak? \nEnter here: ")
        if x == "q":
            engine.say("Bye!")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()

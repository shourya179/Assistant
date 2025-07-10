import speech_recognition as sr
import webbrowser
import pyttsx3
import random

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):  
    engine.say(text)
    engine.runAndWait()
    
def processcommand(c):
    if c.lower() == "open google":
        speak("opening google")
        webbrowser.open("https://www.google.com")
    elif c.lower() == "open youtube":
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com")  
    elif c.lower() == "open facebook":
        speak("opening facebook")
        webbrowser.open("https://www.facebook.com")
    elif c.lower() == "open instagram": 
        speak("opening instagram")
        webbrowser.open("https://www.instagram.com")  
def tell_joke():
    jokes =[

    "Why did the computer go to the doctor? Because it had a virus!"
    "Why don't programmers like nature? It has too many bugs!",
    "Why did the computer go to therapy? It had too many windows open!",
    "What is a programmer's favorite place to hang out? The Foo Bar!"
    ]
    joke = random.choice(jokes)

    speak(joke)    
     
if __name__ == "__main__":
   speak("initilizing jarvis ....")
   ##listen for the wake word "jarvis"
   while True:
        r = sr.Recognizer()
      

        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("leastening...")
                audio = r.listen(source) 
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                
                print("yes")

                #lisen for the command after the wake word
                with sr.Microphone() as source:
                    print("jarvis active ...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)

        except Exception as e:
                print("google error; {0}".format(e))
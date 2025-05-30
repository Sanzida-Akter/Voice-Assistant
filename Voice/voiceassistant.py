import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import requests
import randfacts
from news import *
from weather import *
from jokes import *


listener = aa.Recognizer()

machine = pyttsx3.init()
rate = machine.getProperty('rate')
machine.setProperty('rate', 130)
voices = machine.getProperty('voices')
machine.setProperty('voice', voices[1].id)

def talk(text):
    machine.say(text)
    machine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        return "morning"
    elif 12 <= hour < 16:
        return "afternoon"
    else:
        return "evening"

talk("Hello Sir, good " + wish() + ". I am your voice assistant, Nibu. How are you?")

def input_instruction():
    try:
        with aa.Microphone() as origin:
            print("listening..")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()

    except:
        pass
    return instruction

def play_Jarvis():
    instruction = input_instruction()
    print(instruction)
    if "what" and "about" and "you" in instruction:
        talk("I am having a good day, Sir")

    talk("What can I do for you?")

    while True:
        instruction = input_instruction()
        print(instruction)
        if "play" in instruction:
            talk("Which video do you want to play?")
            with aa.Microphone() as origin:
                print("listening..")
                speech = listener.listen(origin)
                song = listener.recognize_google(speech)
                talk("playing " + song)
                pywhatkit.playonyt(song)

        elif 'time' in instruction:
            time = datetime.datetime.now().strftime('%I %M%p')
            talk('Current time is ' + time)

        elif 'date' in instruction:
            date = datetime.datetime.now().strftime('%d %B %Y')
            talk("Today's date is " + date)

        elif 'how are you' in instruction:
            talk('I am fine, what about you?')

        elif 'what is your name' in instruction:
            talk('I am Nibu, Sir. How can I help you?')

        elif 'information' in instruction:
            talk("You need information related to which topic?")
            with aa.Microphone() as origin:
                print("listening..")
                speech = listener.listen(origin)
                humann = listener.recognize_google(speech)
                info = wikipedia.summary(humann, 3)
                print(info)
                talk(info)

        elif 'news' in instruction:
            print("Sure Sir. I will read latest news for you now ")
            talk("Sure Sir. I will read latest news for you now ")
            arr = news()
            for i in range(len(arr)):
                print(arr[i])
                talk(arr[i])

        elif 'weather' in instruction:
            talk("Weather of which city do you want to know?")
            with aa.Microphone() as origin:
                print("listening..")
                speech = listener.listen(origin)
                city = listener.recognize_google(speech)
                api_address = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=7ed5d716646a3e4c917e9f67f4681679'
                json_data = requests.get(api_address).json()

                def temp():
                    temperature = round(json_data["main"]["temp"] - 273.15, 1)
                    return temperature

                def des():
                    description = json_data["weather"][0]["description"]
                    return description

                print(f"Ok. Temperature in {city} is {temp()} degree Celsius and It will remain {des()}")
                talk(f"Ok. Temperature in {city} is {temp()} degree Celsius and It will remain {des()}")

        elif 'jokes' in instruction:
            url = 'https://official-joke-api.appspot.com/random_joke'
            json_data = requests.get(url).json()
            arr = ["", ""]
            arr[0] = json_data["setup"]
            arr[1] = json_data["punchline"]

            def joke():
                return arr

            jk = joke()
            print(jk)
            talk(jk)
            talk("ha ha ha")

        elif 'fact' in instruction or 'facts' in instruction:
            x = randfacts.getFact()
            print(x)
            talk("Did you know that, " + x)

        elif 'thank you' in instruction:
            talk("My Pleasure,Sir")
            break

        else:
            talk('Please repeat')

play_Jarvis()

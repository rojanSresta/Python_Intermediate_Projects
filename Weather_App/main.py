import requests
import json
import pyttsx3

apiKey = "your_api_key"
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def voice_mode(temp, city):
    engine.say(f"{city} named city not found. Please try valid city name" if temp is None else f"Temperature of {city} is : {temp}\u00B0C")
    engine.runAndWait()

def fetch_weather(userChoice):
    try:
        while True:
            city = input("Enter the city: ")
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric"
            response = requests.get(url)
            data = json.loads(response.text) #-->this data is got by converting the string into dictionary using json.loads

            # normal if else
            # if(temp := data.get('main', {}).get('temp'))==None: #-->used walrus operator
            #     print(f"{city} named city not found.")
            # else:
            #     print(f"Temperature: {temp}\u00B0C")

            # using ternary operator
            temp = data.get('main', {}).get('temp')
            print(f"{city} named city not found." if temp is None else f"Temperature: {temp}\u00B0C") #-->code to show degree
            if userChoice == 'y': voice_mode(temp, city)

            quit = input("Want to quit? (y or n): ")
            match quit:
                case 'y':
                    break
                case 'n':
                    continue
                case _:
                    print("Please enter small y or small n only!")

    except:
        print("Error occured while fetching the weather!")

def voice_or_text():
    userChoice = input("You want to activate voice mode? (y or n): ")
    if userChoice == 'y':
        engine.say("Welcome to weather app. You can type city name and know it's weather condition. Hope you enjoy our app.")
        engine.runAndWait()
    fetch_weather(userChoice)    

voice_or_text()
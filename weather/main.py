import requests
import json
import pyttsx3

city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=615ea523629e42a4b05145050230408&q={city}"

r = requests.get(url)
w_dict = json.loads(r.text)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)

temp = w_dict["current"]["temp_c"]
engine.say(f"The current temparature in {city} is {temp} degree celcius")
engine.runAndWait()
# print(w_dict["current"]["temp_c"])


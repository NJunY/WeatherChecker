from gtts import gTTS
import tensorflow
import playsound
import os
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    print("Searching in google......\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select("#wob_dc")[0].getText().strip()
    weather = soup.select("#wob_tm")[0].getText().strip()
    return location, time, info, weather

print("enter the city name")
city = input()
city=city+" weather"
l, t, i, w = weather(city)
report = "The weather for "+l+" is "+i+", "+w+" degree celcius."

def speak(text):
    try:
        os.remove("voice.mp3")
    except:
        pass
    tts = gTTS(text=text)
    filename = "voice.mp3"
    tts.save(filename)
    print(text)
    playsound.playsound(filename)

speak(report)

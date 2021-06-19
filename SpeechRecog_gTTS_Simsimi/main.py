# API key IIqs5A752QrZxXtgyE1LP9w_xepnmrnXCihFKhPK
import json

import speech_recognition as sr
import pyaudio
from gtts import gTTS
import os
import requests
from pip._vendor.distlib.compat import raw_input

filename = 'audio.mp3'


def reading(text):
    audio = gTTS(text=text, lang='en', slow=False)
    audio.save(filename)
    os.system(f'start {filename}')

while True:
    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     print('You: ')
    #     audio = r.listen(source, phrase_time_limit=2)
    #     try:
    #         text = r.recognize_google(audio)
    #         print(text)
    #         url = 'https://api.simsimi.net/v1/?text=%22' + text + '%20sim%22&lang=en&cf=false'
    #         response = requests.get(url)
    #         response = json.loads(response.text)
    #         print('Sim: ',response['success'])
    #     except:
    #         print('Cant')
    bot_ear = sr.Recognizer()
    with sr.Microphone() as mic:
        print("\nSiri: I'm listening")
        # audio = bot_ear.listen(mic)
        audio = bot_ear.record(mic,
                                    duration=3)
    try:
        text = bot_ear.recognize_google(audio, language='vi-VN')
        print("\nYou: " + text)
        url = 'https://api.simsimi.net/v1/?text=%22' + text + '%20sim%22&lang=en&cf=false'
        response = requests.get(url)
        response = json.loads(response.text)
        print('Sim: ', response['success'])
    except sr.UnknownValueError:
        print("Google Speech Recognition did not understand audio")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))


# while True:
#     message = raw_input('You: ')
#     url = 'https://simsumi.herokuapp.com/api?text='+message+'&lang=en'
#     response = requests.get(url)
#     response = json.loads(response.text)
#     print('Sim: ',response['success'])
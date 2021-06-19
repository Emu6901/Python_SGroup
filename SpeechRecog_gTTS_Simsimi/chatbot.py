import json

import speech_recognition as sr

from gtts import gTTS
import os
import requests
from playsound import playsound


class SpeechToText:
    def __init__(self):
        self.bot_ear = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as mic:
            print("\nSiri: I'm listening")
            # audio = bot_ear.listen(mic)
            audio = self.bot_ear.record(mic,
                                        duration=3)
        try:
            you = self.bot_ear.recognize_google(audio, language='vi-VN')
            print("\nYou: " + you)
            return you
        except sr.UnknownValueError:
            print("Google Speech Recognition did not understand audio")
            return ''
        except sr.RequestError as e:
            print("Request Failed; {0}".format(e))
            return ''


class TextToSpeech:
    def __init__(self, lang):
        self.filename = 'audio.mp3'
        self.lang = lang

    def talk(self, text):
        audio = gTTS(text=text, lang=self.lang, slow=False)
        os.remove(self.filename)
        audio.save(self.filename)
        playsound(self.filename)


class ChatBot:
    def __init__(self, lang='en'):
        self.lang = lang
        self.headers = {
            'Content-Type': 'application/json',
            'x-api-key': 'IIqs5A752QrZxXtgyE1LP9w_xepnmrnXCihFKhPK',
            'charset': 'utf-8'
        }
        self.url = 'https://wsapi.simsimi.com/190410/talk'

    def getrespond(self, message):
        data = '{\n            "utext": "' + message + '", \n            "lang": "' + self.lang + '" \n     }'
        response = requests.post('https://wsapi.simsimi.com/190410/talk', headers=self.headers,
                                 data=data.encode('utf-8'))
        if response.status_code == 200:
            response = json.loads(response.text)
            print('Sim:', response['atext'])
            return response['atext']
        return ''

    def run(self):
        listening = True
        tt = SpeechToText()
        ts = TextToSpeech('vi')
        while listening:
            message = tt.listen()
            if message == 'dừng lại':
                listening = False
            if message == '':
                input("Press Enter to continue...")
            respond = self.getrespond(message)
            if respond != '':
                ts.talk(respond)


if __name__ == "__main__":
    chatbot = ChatBot('vi')
    chatbot.run()

from threading import Thread
from time import sleep

import requests

BASE_URL = r'https://606b1c60f8678400172e5a1d.mockapi.io/api/'
last_msg_id = "0"


def post_msg():
    while True:
        msg = input()
        requests.post(BASE_URL + r'myapi', {
            'userID': 'minh',
            'message': msg,
        })


def get_msg():
    global last_msg_id
    while True:
        sleep(2)
        response = requests.get(BASE_URL + r'myapi').json()
        if response == []:
            continue
        tmp = last_msg_id
        for item in response:
            if int(item["id"]) <= int(tmp):
                continue
            if item['id'] != last_msg_id:
                print(item['userID'], '   ', item['message'])
                last_msg_id = item['id']


# class myClassA(Thread):
#     def __init__(self):
#         Thread.__init__(self)
#         self.daemon = True
#         self.start()
# 
#     def run(self):
#         while True:
#             post_msg()
# 
# 
# class myClassB(Thread):
#     def __init__(self):
#         Thread.__init__(self)
#         self.daemon = True
#         self.start()
# 
#     def run(self):
#         while True:
#             get_msg()


# myClassA()
# myClassB()
thread1 = Thread(target=post_msg, daemon=True)
thread2 = Thread(target=get_msg, daemon=True)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

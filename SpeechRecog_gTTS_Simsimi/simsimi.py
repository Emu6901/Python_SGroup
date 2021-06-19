import json

import requests
from pip._vendor.distlib.compat import raw_input

message = raw_input('You: ')
headers = {
    'Content-Type': 'application/json',
    'x-api-key': 'IIqs5A752QrZxXtgyE1LP9w_xepnmrnXCihFKhPK',
}

data = '{\n            "utext": "'+message+'", \n            "lang": "vi" \n     }'
print(data)
response = requests.post('https://wsapi.simsimi.com/190410/talk', headers=headers, data=data.encode('utf-8'))
for i in response:
    print(i)
response = json.loads(response.text)
print('Sim:', response['atext'])
import json
import requests

class DownloadCovidInfo:

    def __init__(self, url):
        self.url = url

    def get_all_data(self):
        return requests.get(self.url).json()

    def get_data_by_country(self, name):
        for i in requests.get(self.url).json()["Countries"]:
            if i['Country'] == name:
                return i

    def save_to_file(self):
        response = requests.get(self.url).json()
        with open('output.json', 'w') as f:
            json.dump(response, f, indent=4)


url = "https://api.covid19api.com/summary"
info = DownloadCovidInfo(url)
print(info.url)
print(info.get_all_data())
print(info.get_data_by_country('Viet Nam'))
info.save_to_file()

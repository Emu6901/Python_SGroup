import requests
from bs4 import BeautifulSoup

response = requests.get('https://shopee.vn/flash_sale')
soup = BeautifulSoup(response.text, features='html.parser')
infos = soup.find_all(class_='flash-sale-item-card__item-name-box')
for info in infos:
    print(info.get('value'))
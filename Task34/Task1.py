import requests
URL = 'https://ru.wikipedia.org/wiki/Python'

with open('Robots.txt', "r+", encoding='utf-8') as file:
    paste_website = requests.get(URL)
    file.write(paste_website.text)
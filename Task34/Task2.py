import requests
import json

URL = 'https://api.pushshift.io/reddit/comment/search/'

with open('subreddit.json', 'r+', encoding='UTF-8') as file:
    data = requests.get(URL, {'subreddit': 'python'})
    data = data.json()
    file_serializ = data
    file.seek(0)
    file.truncate(0)
    json.dump(file_serializ, file, indent=4)
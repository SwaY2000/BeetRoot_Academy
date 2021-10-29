import requests
import threading
import json

class MyThreader(threading.Thread):
    def __init__(self, URL, params):
        threading.Thread.__init__(self)
        self.url = URL
        self.params = params
        self.variable = []

    def run(self) -> None:
        print(f"Starting {self.name}")
        paste_website = requests.get(self.url)
        paste_website = paste_website.json()
        temp = paste_website['data']
        for i in temp:
            self.variable.append(i[self.params])
        print(f"Finished {self.name}")

thread1 = MyThreader('https://api.pushshift.io/reddit/comment/search/', 'author')
thread2 = MyThreader('https://api.pushshift.io/reddit/comment/search/', 'body')
thread1.start()
thread2.start()

with open('file.json', "r+", encoding='utf-8') as file:
    thread1.join()
    thread2.join()
    append_json = {}

    for i, j in zip(thread1.variable, thread2.variable):
        append_json.update({i:j})
        print(append_json)

    file_serializ = json.load(file)
    print(file_serializ)
    file_serializ["author"].update(append_json)
    file.seek(0)
    file.truncate(0)
    json.dump(file_serializ, file, indent=1)

print('Done')

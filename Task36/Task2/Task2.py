import concurrent.futures, multiprocessing, requests, os
import json

URL = 'https://api.pushshift.io/reddit/comment/search/'

PARAMS = ['author', 'body']



global dict_for_json

dict_for_json = {1:1}

def download(URL, param):
    print(dict_for_json)
    print(f'Starting {os.getpid()}, parent {os.getppid()}')
    temp = requests.get(URL)
    temp = temp.json()
    temp = temp['data']
    temp_out = []
    for i in temp:
        temp_out.append(i[param])
    dict_for_json[param] = temp_out
    print(dict_for_json)
    return dict_for_json

if __name__ == '__main__':
    with open('task2.json', 'r+', encoding='UTF-8') as file:
        file_ser = json.load(file)

        manager = multiprocessing.Manager()
        process_itter = []


        for i in range(len(PARAMS)):
            p = multiprocessing.Process(target=download, args=(URL, PARAMS[i]))
            process_itter.append(p)
            p.start()

        for proc in process_itter:
            proc.join()

        file.seek(0)
        file.truncate(0)
        print(dict_for_json)
        json.dump(dict_for_json, file, indent=1)

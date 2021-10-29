import asyncio, aiohttp, urllib.request, time, os, json

URL = 'https://api.pushshift.io/reddit/comment/search/'
MAX_CLIENTS = 3

async def asynchronous():
    start = time.time()
    tasks = [asyncio.ensure_future(connection(URL, i)) for i in range(MAX_CLIENTS)]
    await asyncio.wait(tasks)
    print(f'Connection ended with process: {os.getpid()}, Time work: {time.time()-start}')

async def connection(url, name_process):
    print(f'Connection start with process: {os.getpid()}, Name: {name_process}')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            json_saver = await resp.json()
            print(json_saver)
    async with open("task2.json", "r+") as json_file:
        json_file_serialize = json.load(json_file)
        json_file_serialize.update(json_saver)
        json_file.seek(0)
        json_file.read(0)
        try:
            json.dump(json_file, json_file_serialize)
        except:
            print('Exception')
            pass

loop = asyncio.new_event_loop()
loop.run_until_complete(asynchronous())


import socket
import asyncio
from json import dump, load
from time import gmtime, strftime
from CONGIF import SERVER, MAX_CONNECTION, LIST_CONNECTIONS, MAX_SAVE_HISTORY

async def handle_connection(connection, clients: list = LIST_CONNECTIONS):
    clients.append(connection)
    loop = asyncio.get_event_loop()
    while True:
        try:
            data = await loop.sock_recv(connection, 1024)
            await asyncio.gather(
                *[loop.sock_sendall(client, data) for client in clients]
                )
            with open('history.json', 'r+') as json_file:
                json_serializ = load(json_file)
                time_and_messages = {(strftime("%Y-%m-%d %H:%M:%S", gmtime())): data.decode('utf-8')}
                print(time_and_messages)
                json_serializ.update(time_and_messages)
                while True:
                    if len(json_serializ) > MAX_SAVE_HISTORY:
                        item_which_pop = 0
                        item_for_pop = list(json_serializ.keys())[item_which_pop]
                        json_serializ.pop(item_for_pop)
                    else:
                        break
                json_file.truncate(0)
                json_file.seek(0)
                dump(json_serializ, json_file, indent=1)
        except:
            connection.close()
            clients.remove(connection)
            break

async def main(server: tuple = SERVER, max_connection: int = MAX_CONNECTION):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    loop = asyncio.get_event_loop()
    sock.bind(server)
    sock.setblocking(False)
    sock.listen(max_connection)
    while True:
        connection, client = await loop.sock_accept(sock)
        with open('history.json', 'r+') as json_file:
            json_serializ = load(json_file)
            messages_history = ''
            for i in json_serializ:
                messages_history = (f'{messages_history}'+'\n'+f'{json_serializ[i]}')
            print(messages_history)
            await loop.sock_sendall(connection, messages_history.encode('utf-8'))
        loop.create_task(
            handle_connection(connection)
        )

if __name__ == '__main__':
    asyncio.run(main())
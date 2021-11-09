import socket, json, threading
from CONGIF import SERVER, ACCOUNT_JSON

class ChatsRoom():
    def __init__(self):
        """Starting chats, user must choose, log in or registration in app """
        while True:
            print(f'Hello! You have account?', '\n', '"y" - yes, i have, "n" - no, i dont have')
            answer = input().lower()
            if answer == 'y':
                self._log_in()
                break
            elif answer == 'n':
                self._create_account()
                break
            else:
                print('I don`t have such function')
        self._connection()

    def _log_in(self):
        """This is function check your username in Base, if base have username, then program
        check correct input password, if password unccorrect, method Json.read return False, if correct
        - return True"""
        while True:
            self.login = input('Your username')
            self.password = input('Your password')
            if Json.read(self.login, self.password) == True:
                print('You log in your account')
                break
            else:
                print('Not found account or uncorrect password')

    def _create_account(self):
        """This is function dump username and password for new user with help method Json.write"""
        while True:
            self.login = input('Your username: ')
            self.password = input('Your password: ')
            if Json.write(self.login, self.password) is True:
                break

    def _connection(self, server: tuple = SERVER):
        """It`s function create socket for connection and split on thread receive and send messages"""
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(server)
        data = client_socket.recv(1024)
        print('Recently history messages', '\n', data.decode('utf-8'))
        try:
            messages = threading.Thread(target=self.send, args=(server, client_socket,))
            messages.start()

            data = threading.Thread(target=self.receive, args=(1024, client_socket,))
            data.start()
        except:
            print('server error')

    def send(self, server, client_socket):
        """Function sending messages on chatroom server"""
        while True:
            messages = input(f'{self.login}>>')
            messages = f'{self.login}: {messages}'.encode('utf-8')
            client_socket.sendto(messages, server)

    def receive(self, size_messages, client_socket):
        """Function receive messages from chatroom server"""
        while True:
            data = client_socket.recv(size_messages)
            print('\n', data.decode('utf-8'), sep='', end='')

class Json:
    PATH_TO_JSON = 'clients.json'
    @staticmethod
    def read(login, password):
        """"Function check registration user already and correct password"""
        with open(ACCOUNT_JSON, 'r+') as json_file:
            print('im here')
            json_file_serial = json.load(json_file)

            if login in json_file_serial:
                print('find')
                if json_file_serial[login] == password:
                    print('auth')
                    return True
            else:
                return False
    @staticmethod
    def write(login, password):
        """Create new account"""
        with open(ACCOUNT_JSON, 'r+') as json_file:
            if Json.read(login, password) is False:
                json_file_serial = json.load(json_file)
                temp = {login: password}
                json_file_serial.update(temp)
                json_file.truncate(0)
                json_file.seek(0)
                json.dump(json_file_serial, json_file, indent=1)
                return True
            else:
                print('This is username already registered, choose any username')
                return False

if __name__ == '__main__':
    ChatsRoom()


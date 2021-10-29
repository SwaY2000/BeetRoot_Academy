import socket
import threading

class ThreadServer(threading.Thread):
    def __init__(self, client_address, client_socket):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.client_address = client_address
        print(f"New connection{self.client_address}")

    def run(self):
        print(f"Connection from: {self.client_address}")
        msg = ''
        while True:
            data = self.client_socket.recv(2048)
            msg = data.decode()
            if msg == 'bye':
                break
            print("from client", msg)
            self.client_socket.send(bytes(msg, 'UTF-8'))
        print("Client at ", self.client_address, " disconnected...")

HOST = 'localhost'
PORT = 9090

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    print("Server started")
    print("Waiting for client request..")
    while True:
        s.listen(2)
        conn, addr = s.accept()
        server_thread = ThreadServer(conn, addr)
        server_thread.start()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data.upper())


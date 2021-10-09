import socket

UDP_IP_ADDRESS = "localhost"
UDP_PORT = 55000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as serverSock:
    serverSock.bind((UDP_IP_ADDRESS, UDP_PORT))
    while True:
        data, addr = serverSock.recvfrom(1024)
        print ("IP-addres: ", addr[0], "Port: ", addr[1],  "Message: ", data, sep = "\n")
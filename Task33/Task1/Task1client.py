import socket

UDP_IP_ADDRESS = "localhost"
UDP_PORT = 55000


Message = input()
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientSock.sendto(Message.encode('utf-8'), (UDP_IP_ADDRESS, UDP_PORT))
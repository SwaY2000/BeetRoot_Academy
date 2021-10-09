import socket

UDP_IP_ADDRESS = "localhost"
UDP_PORT = 55000

while True:
    choose = input('Encode or decode')
    string = input('Input your message')
    step_encode = input('Input your step for code')
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSock.sendto(choose.encode('utf-8'), (UDP_IP_ADDRESS, UDP_PORT))
    clientSock.sendto(string.encode('utf-8'), (UDP_IP_ADDRESS, UDP_PORT))
    clientSock.sendto(step_encode.encode('utf-8'), (UDP_IP_ADDRESS, UDP_PORT))
    ack_msg = clientSock.recv(1024).decode('utf-8')
    print(ack_msg)
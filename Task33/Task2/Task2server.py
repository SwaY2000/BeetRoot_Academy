import socket

UDP_IP_ADDRESS = "localhost"
UDP_PORT = 55000

def encode_cessar(string: str, step_encode):
    """Encode string with algorithms 'Encode Cessar'"""
    string = string.upper()
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    step_encode = int(step_encode)
    encode_string = ''

    for item in string:
        if item in ALPHABET:
            try:
                encode_string += ALPHABET[ALPHABET.index(item)+step_encode]
            except IndexError:
                counter_max = len(ALPHABET)-1
                counter_min = ALPHABET.index(item)
                temp_encode = step_encode-1
                while counter_max > counter_min:
                    counter_min += 1
                    temp_encode -= 1
                encode_string += ALPHABET[temp_encode]
        else:
            encode_string += item
    return encode_string

def decode_cessar (string: str, step_decode):
    """Decode string with algorithms 'Encode Cessar'"""
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    step_decode = int(step_decode)
    decode_string = ''

    for item in string:
        if item in ALPHABET:
            decode_string += ALPHABET[ALPHABET.index(item)-step_decode]
        else:
            decode_string += item
    return decode_string


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as serverSock:
    serverSock.bind((UDP_IP_ADDRESS, UDP_PORT))
    while True:
        choose, addr = serverSock.recvfrom(1024)
        string = serverSock.recvfrom(1024)
        step_encode = serverSock.recvfrom(1024)

        string = string[0]

        if (choose.decode('UTF-8')).lower() == "encode":
            print('encode')
            string = encode_cessar(string.decode('UTF-8'), step_encode[0])
        else:
            print('decode')
            string = decode_cessar(string.decode('UTF-8'), step_encode[0])

        print("IP-addres: ", addr[0], "Port: ",
              addr[1], "Message: ", string, sep="\n")

        serverSock.sendto(string.encode('UTF-8'), addr)

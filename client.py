from socket import *


if __name__ == '__main__':
    sock = socket()
    sock.connect(('localhost', 9090))
    sock.send(b'hello, world!')

    data = sock.recv(1024)
    sock.close()

    print(data)
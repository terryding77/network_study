from __future__ import print_function

from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('localhost', 5277))
import time

time.sleep(2)
clientSock.send('GET /in HTTP/1.1\nHost: localhost:5277')
while True:
    buf = (clientSock.recv(1024))
    if len(buf):
        # print buf,
        print(buf, end="")
    else:
        break
clientSock.close()

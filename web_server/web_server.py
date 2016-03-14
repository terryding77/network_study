# import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
serverSocket.bind(('localhost', 5277))
serverSocket.listen(10)
# Fill in end
while True:
    # Establish the connection
    print 'Ready to serve...'
    # Fill in start
    connectionSocket, addr = serverSocket.accept()
    # Fill in end
    try:
        # Fill in start
        message = connectionSocket.recv(1024)
        print(message)
        # Fill in end
        filename = message.split()[1]
        print(filename)
        f = open(filename[1:])
        # Fill in start
        outputdata = f.read()
        # Fill in end
        # Send one HTTP header line into socket
        # Fill in start
        import datetime
        GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
        date_now = datetime.datetime.utcnow().strftime(GMT_FORMAT)
        response = "HTTP/1.1 200 OK\nContent-Type:text/html\nDate: "+date_now+"\n\n"
        connectionSocket.sendall(response)
        # Fill in end
        # Send the content of the requested file to the client
        # connectionSocket.sendall(outputdata)
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        import datetime
        GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
        date_now = datetime.datetime.utcnow().strftime(GMT_FORMAT)
        response = "HTTP/1.1 404 Not Found\nDate: "+ date_now
        connectionSocket.sendall(response)
        # Fill in end
        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end
    except:
        import datetime
        GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
        date_now = datetime.datetime.utcnow().strftime(GMT_FORMAT)
        response = "HTTP/1.1 404 Not Found\nDate: "+ date_now
        connectionSocket.sendall(response)
        connectionSocket.close()
serverSocket.close()

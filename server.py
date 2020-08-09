from socket import *
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8080))
serverSock.listen(1)

clientSock, addr = serverSock.accept()

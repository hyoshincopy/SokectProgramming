from socket import *
serverSock = socket(AF_INET, SOCK_STREAM)  # ? (1)소켓 생성
serverSock.bind(('', 8080))  # ? bind => (ip,port)인 튜플을 address family에 연결
serverSock.listen(1)  # ? 상대방의 접속을 기다림 => listen 의 매개변수는 동시접속 개수
clientSock, addr = serverSock.accept()

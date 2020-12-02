from socket import *

tcp_socket = socket(AF_INET,SOCK_STREAM)

tcp_socket.bind(("0.0.0.0",8888))

tcp_socket.listen(5)

while True:
    print("waiting for connecting...")
    connfd,addr=tcp_socket.accept()
    print("connect from",addr)

    while True:
        data=connfd.recv(1024)
        print("receive",data.decode())
        if data== b"##":
            break
        connfd.send(b"Thanks")
    connfd.close()


tcp_socket.close()



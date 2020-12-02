from socket import *

tcp_socket=socket()

tcp_socket.connect(("127.0.0.1",8888))

while True:
    data=input(">>")
    tcp_socket.send(data.encode())
    if data == "##":
        break
    data= tcp_socket.recv(1024)
    print("from server:",data.decode())


tcp_socket.close()
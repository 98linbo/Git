from socket import *

udp_sock = socket(AF_INET,SOCK_DGRAM)
udp_sock.bind(("127.0.0.1",3333))
ADDR = ("127.0.0.1",3333)


while True:
    # 发送数据192.168.185.215
    data = input("word:")
    # 直接回车，客户端结束
    if not data:
        break

    udp_sock.sendto(data.encode(),ADDR)
    # if data == "##":
    #     break

    # 接收
    data,addr = udp_sock.recvfrom(1024)
    print("word:",data.decode())

udp_sock.close()



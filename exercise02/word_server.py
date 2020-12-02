from socket import *
import re
import pymysql

udp_sock = socket(AF_INET,SOCK_DGRAM)
udp_sock.bind(("0.0.0.0",3333))

while True:
    # 接收数据  recvfrom 阻塞等待
    data,addr = udp_sock.recvfrom(1024)
    print(addr,"接收到：",data.decode()) # data --> bytes

    args = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "123456",
        "database": "dict",
        "charset": "utf8"
    }

    db = pymysql.connect(**args)
    cur = db.cursor()

    cur.execute(f"select * from word where word='{data.decode()}'")
    print(cur.fetchall())

    # 发送数据 发送字节串
    n = udp_sock.sendto(cur.fetchall(),addr)


# 关闭套接字
udp_sock.close()
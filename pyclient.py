#-*- coding:utf-8 -*-


from socket import *

# from pip._vendor.distlib.compat import raw_input

# HOST = 'localhost'

HOST = '192.168.1.11'
#HOST = '202.106.46.152'
# HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = raw_input('>')
    if not data:
        break
    tcpCliSock.send('%s\r\n' % data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.strip())
    tcpCliSock.close()

#
# import socket
#
# import sys
#
# #HOST = 'localhost'
# HOST = '172.31.99.170'
# PORT = 12356
# ADDR =(HOST,PORT)
# BUFSIZE = 1024
#
# sock = socket.socket()
# try:
#     a = sock.connect(ADDR)
# except Exception,e:
#     print 'error',e
#     sock.close()
#     sys.exit()
#
# print 'have connected with server'
#
# while True:
#     data = raw_input('> ')
#     if len(data)>0:
#         print 'send:',data
#         sock.sendall(data) #不要用send()
#         recv_data = sock.recv(BUFSIZE)
#         print 'receive::',recv_data
#     else:
#         sock.close()
#         break

# import socket
#
# HOST = '172.31.99.170'  # 定义目标主机名
# PORT = 50007  # 定义目标主机开放服务端口号
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 选择Socket类型和Socket数据包类型
# s.connect((HOST, PORT))  # 连接到目标主机的socket（套接字）中
#
# s.sendall('Hello, world!')  # 发送数据
# data = s.recv(1024)  # 接收数据
# s.close()  # 关闭socket
# print 'Received', repr(data)
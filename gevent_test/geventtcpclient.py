from socket import *
clientSocket = socket(AF_INET,SOCK_STREAM)
"""gevent客户端 tcp 客户端"""

#连接到服务器
serverAddr = ('192.168.0.116',17788)
clientSocket.connect(serverAddr)
while True:
	msg = input(">>")
	#发送数据
	clientSocket.send(msg.encode())
	#接收数据
	recvData = clientSocket.recv(1024)
	print("<<%s"%recvData)
	if msg == "bye":
		break
clientSocket.close()


